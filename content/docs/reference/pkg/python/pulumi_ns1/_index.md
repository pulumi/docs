---
title: Package pulumi_ns1
title_tag: Package pulumi_ns1 | Python SDK
linktitle: pulumi_ns1
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "ns1" >}}

<div class="section" id="pulumi-ns1">
<h1>Pulumi NS1<a class="headerlink" href="#pulumi-ns1" title="Permalink to this headline"></a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-ns1">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-ns1/issues">pulumi/pulumi-ns1 repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-ns1/issues">terraform-providers/terraform-provider-ns1 repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_ns1"></span><dl class="py class">
<dt id="pulumi_ns1.APIKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">APIKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_strict</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.APIKey" title="Permalink to this definition"></a></dt>
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
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the apikey may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the apikey may not access.</p></li>
<li><p><strong>ip_whitelist_strict</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets exclusivity on this IP whitelist.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
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
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The teams that the apikey belongs to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_ns1.APIKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_strict</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.APIKey" title="pulumi_ns1.APIKey">APIKey</a><a class="headerlink" href="#pulumi_ns1.APIKey.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing APIKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the apikey may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the apikey may not access.</p></li>
<li><p><strong>ip_whitelist_strict</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets exclusivity on this IP whitelist.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
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
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The teams that the apikey belongs to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.account_manage_account_settings">
<em class="property">property </em><code class="sig-name descname">account_manage_account_settings</code><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_account_settings" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify account settings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.account_manage_apikeys">
<em class="property">property </em><code class="sig-name descname">account_manage_apikeys</code><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_apikeys" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify account apikeys.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.account_manage_payment_methods">
<em class="property">property </em><code class="sig-name descname">account_manage_payment_methods</code><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_payment_methods" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify account payment methods.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.account_manage_plan">
<em class="property">property </em><code class="sig-name descname">account_manage_plan</code><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_plan" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify the account plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.account_manage_teams">
<em class="property">property </em><code class="sig-name descname">account_manage_teams</code><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_teams" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify other teams in the account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.account_manage_users">
<em class="property">property </em><code class="sig-name descname">account_manage_users</code><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_users" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify account users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.account_view_activity_log">
<em class="property">property </em><code class="sig-name descname">account_view_activity_log</code><a class="headerlink" href="#pulumi_ns1.APIKey.account_view_activity_log" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can view activity logs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.account_view_invoices">
<em class="property">property </em><code class="sig-name descname">account_view_invoices</code><a class="headerlink" href="#pulumi_ns1.APIKey.account_view_invoices" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can view invoices.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.data_manage_datafeeds">
<em class="property">property </em><code class="sig-name descname">data_manage_datafeeds</code><a class="headerlink" href="#pulumi_ns1.APIKey.data_manage_datafeeds" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify data feeds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.data_manage_datasources">
<em class="property">property </em><code class="sig-name descname">data_manage_datasources</code><a class="headerlink" href="#pulumi_ns1.APIKey.data_manage_datasources" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify data sources.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.data_push_to_datafeeds">
<em class="property">property </em><code class="sig-name descname">data_push_to_datafeeds</code><a class="headerlink" href="#pulumi_ns1.APIKey.data_push_to_datafeeds" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can publish to data feeds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.dhcp_manage_dhcp">
<em class="property">property </em><code class="sig-name descname">dhcp_manage_dhcp</code><a class="headerlink" href="#pulumi_ns1.APIKey.dhcp_manage_dhcp" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can manage DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.dhcp_view_dhcp">
<em class="property">property </em><code class="sig-name descname">dhcp_view_dhcp</code><a class="headerlink" href="#pulumi_ns1.APIKey.dhcp_view_dhcp" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can view DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.dns_manage_zones">
<em class="property">property </em><code class="sig-name descname">dns_manage_zones</code><a class="headerlink" href="#pulumi_ns1.APIKey.dns_manage_zones" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify the accounts zones.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.dns_view_zones">
<em class="property">property </em><code class="sig-name descname">dns_view_zones</code><a class="headerlink" href="#pulumi_ns1.APIKey.dns_view_zones" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can view the accounts zones.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.dns_zones_allow_by_default">
<em class="property">property </em><code class="sig-name descname">dns_zones_allow_by_default</code><a class="headerlink" href="#pulumi_ns1.APIKey.dns_zones_allow_by_default" title="Permalink to this definition"></a></dt>
<dd><p>If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.dns_zones_allows">
<em class="property">property </em><code class="sig-name descname">dns_zones_allows</code><a class="headerlink" href="#pulumi_ns1.APIKey.dns_zones_allows" title="Permalink to this definition"></a></dt>
<dd><p>List of zones that the apikey may access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.dns_zones_denies">
<em class="property">property </em><code class="sig-name descname">dns_zones_denies</code><a class="headerlink" href="#pulumi_ns1.APIKey.dns_zones_denies" title="Permalink to this definition"></a></dt>
<dd><p>List of zones that the apikey may not access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.ip_whitelist_strict">
<em class="property">property </em><code class="sig-name descname">ip_whitelist_strict</code><a class="headerlink" href="#pulumi_ns1.APIKey.ip_whitelist_strict" title="Permalink to this definition"></a></dt>
<dd><p>Sets exclusivity on this IP whitelist.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.ip_whitelists">
<em class="property">property </em><code class="sig-name descname">ip_whitelists</code><a class="headerlink" href="#pulumi_ns1.APIKey.ip_whitelists" title="Permalink to this definition"></a></dt>
<dd><p>The IP addresses to whitelist for this key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.ipam_manage_ipam">
<em class="property">property </em><code class="sig-name descname">ipam_manage_ipam</code><a class="headerlink" href="#pulumi_ns1.APIKey.ipam_manage_ipam" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can manage IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.ipam_view_ipam">
<em class="property">property </em><code class="sig-name descname">ipam_view_ipam</code><a class="headerlink" href="#pulumi_ns1.APIKey.ipam_view_ipam" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can view IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_ns1.APIKey.key" title="Permalink to this definition"></a></dt>
<dd><p>The apikeys authentication token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.monitoring_manage_jobs">
<em class="property">property </em><code class="sig-name descname">monitoring_manage_jobs</code><a class="headerlink" href="#pulumi_ns1.APIKey.monitoring_manage_jobs" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify monitoring jobs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.monitoring_manage_lists">
<em class="property">property </em><code class="sig-name descname">monitoring_manage_lists</code><a class="headerlink" href="#pulumi_ns1.APIKey.monitoring_manage_lists" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can modify notification lists.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.monitoring_view_jobs">
<em class="property">property </em><code class="sig-name descname">monitoring_view_jobs</code><a class="headerlink" href="#pulumi_ns1.APIKey.monitoring_view_jobs" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can view monitoring jobs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_ns1.APIKey.name" title="Permalink to this definition"></a></dt>
<dd><p>The free form name of the apikey.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.security_manage_active_directory">
<em class="property">property </em><code class="sig-name descname">security_manage_active_directory</code><a class="headerlink" href="#pulumi_ns1.APIKey.security_manage_active_directory" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can manage global active directory.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.security_manage_global2fa">
<em class="property">property </em><code class="sig-name descname">security_manage_global2fa</code><a class="headerlink" href="#pulumi_ns1.APIKey.security_manage_global2fa" title="Permalink to this definition"></a></dt>
<dd><p>Whether the apikey can manage global two factor authentication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.teams">
<em class="property">property </em><code class="sig-name descname">teams</code><a class="headerlink" href="#pulumi_ns1.APIKey.teams" title="Permalink to this definition"></a></dt>
<dd><p>The teams that the apikey belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.APIKey.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.APIKey.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">AwaitableGetDNSSecResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">delegation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.AwaitableGetDNSSecResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.AwaitableGetRecordResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">AwaitableGetRecordResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">answers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_answers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_client_subnet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.AwaitableGetRecordResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.AwaitableGetZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">AwaitableGetZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">additional_primaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostmaster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nx_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.AwaitableGetZoneResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.DataFeed">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">DataFeed</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataFeed" title="Permalink to this definition"></a></dt>
<dd><p>Provides a NS1 Data Feed resource. This can be used to create, modify, and delete data feeds.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_ns1</span> <span class="k">as</span> <span class="nn">ns1</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">DataSource</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">sourcetype</span><span class="o">=</span><span class="s2">&quot;nsone_v1&quot;</span><span class="p">)</span>
<span class="n">uswest_feed</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">DataFeed</span><span class="p">(</span><span class="s2">&quot;uswestFeed&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;label&quot;</span><span class="p">:</span> <span class="s2">&quot;uswest&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">source_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">useast_feed</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">DataFeed</span><span class="p">(</span><span class="s2">&quot;useastFeed&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;label&quot;</span><span class="p">:</span> <span class="s2">&quot;useast&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">source_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p><a class="reference external" href="https://ns1.com/api#data-feeds">Datafeed Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – The feeds configuration matching the specification in
<code class="docutils literal notranslate"><span class="pre">feed_config</span></code> from /data/sourcetypes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the data feed.</p></li>
<li><p><strong>source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source id that this feed is connected to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_ns1.DataFeed.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.DataFeed" title="pulumi_ns1.DataFeed">DataFeed</a><a class="headerlink" href="#pulumi_ns1.DataFeed.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing DataFeed resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – The feeds configuration matching the specification in
<code class="docutils literal notranslate"><span class="pre">feed_config</span></code> from /data/sourcetypes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the data feed.</p></li>
<li><p><strong>source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source id that this feed is connected to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataFeed.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_ns1.DataFeed.config" title="Permalink to this definition"></a></dt>
<dd><p>The feeds configuration matching the specification in
<code class="docutils literal notranslate"><span class="pre">feed_config</span></code> from /data/sourcetypes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataFeed.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_ns1.DataFeed.name" title="Permalink to this definition"></a></dt>
<dd><p>The free form name of the data feed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataFeed.source_id">
<em class="property">property </em><code class="sig-name descname">source_id</code><a class="headerlink" href="#pulumi_ns1.DataFeed.source_id" title="Permalink to this definition"></a></dt>
<dd><p>The data source id that this feed is connected to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataFeed.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataFeed.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataFeed.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">DataSource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataSource" title="Permalink to this definition"></a></dt>
<dd><p>Provides a NS1 Data Source resource. This can be used to create, modify, and delete data sources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_ns1</span> <span class="k">as</span> <span class="nn">ns1</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">DataSource</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">sourcetype</span><span class="o">=</span><span class="s2">&quot;nsone_v1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p><a class="reference external" href="https://ns1.com/api#data-sources">Datasource Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – The data source configuration, determined by its type,
matching the specification in <code class="docutils literal notranslate"><span class="pre">config</span></code> from /data/sourcetypes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the data source.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data sources type, listed in API endpoint <a class="reference external" href="https://api.nsone.net/v1/data/sourcetypes">https://api.nsone.net/v1/data/sourcetypes</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_ns1.DataSource.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.DataSource" title="pulumi_ns1.DataSource">DataSource</a><a class="headerlink" href="#pulumi_ns1.DataSource.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing DataSource resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – The data source configuration, determined by its type,
matching the specification in <code class="docutils literal notranslate"><span class="pre">config</span></code> from /data/sourcetypes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the data source.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data sources type, listed in API endpoint <a class="reference external" href="https://api.nsone.net/v1/data/sourcetypes">https://api.nsone.net/v1/data/sourcetypes</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataSource.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_ns1.DataSource.config" title="Permalink to this definition"></a></dt>
<dd><p>The data source configuration, determined by its type,
matching the specification in <code class="docutils literal notranslate"><span class="pre">config</span></code> from /data/sourcetypes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataSource.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_ns1.DataSource.name" title="Permalink to this definition"></a></dt>
<dd><p>The free form name of the data source.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataSource.sourcetype">
<em class="property">property </em><code class="sig-name descname">sourcetype</code><a class="headerlink" href="#pulumi_ns1.DataSource.sourcetype" title="Permalink to this definition"></a></dt>
<dd><p>The data sources type, listed in API endpoint <a class="reference external" href="https://api.nsone.net/v1/data/sourcetypes">https://api.nsone.net/v1/data/sourcetypes</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataSource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataSource.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataSource.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">GetDNSSecResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">delegation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.GetDNSSecResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getDNSSec.</p>
<dl class="py method">
<dt id="pulumi_ns1.GetDNSSecResult.delegation">
<em class="property">property </em><code class="sig-name descname">delegation</code><a class="headerlink" href="#pulumi_ns1.GetDNSSecResult.delegation" title="Permalink to this definition"></a></dt>
<dd><p>(Computed) - Delegation field is documented
below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetDNSSecResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_ns1.GetDNSSecResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetDNSSecResult.keys">
<em class="property">property </em><code class="sig-name descname">keys</code><a class="headerlink" href="#pulumi_ns1.GetDNSSecResult.keys" title="Permalink to this definition"></a></dt>
<dd><p>(Computed) - Keys field is documented below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.GetRecordResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">GetRecordResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">answers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_answers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_client_subnet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.GetRecordResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getRecord.</p>
<dl class="py method">
<dt id="pulumi_ns1.GetRecordResult.answers">
<em class="property">property </em><code class="sig-name descname">answers</code><a class="headerlink" href="#pulumi_ns1.GetRecordResult.answers" title="Permalink to this definition"></a></dt>
<dd><p>List of NS1 answers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetRecordResult.filters">
<em class="property">property </em><code class="sig-name descname">filters</code><a class="headerlink" href="#pulumi_ns1.GetRecordResult.filters" title="Permalink to this definition"></a></dt>
<dd><p>List of NS1 filters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetRecordResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_ns1.GetRecordResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetRecordResult.link">
<em class="property">property </em><code class="sig-name descname">link</code><a class="headerlink" href="#pulumi_ns1.GetRecordResult.link" title="Permalink to this definition"></a></dt>
<dd><p>The target record this links to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetRecordResult.meta">
<em class="property">property </em><code class="sig-name descname">meta</code><a class="headerlink" href="#pulumi_ns1.GetRecordResult.meta" title="Permalink to this definition"></a></dt>
<dd><p>Map of metadata</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetRecordResult.regions">
<em class="property">property </em><code class="sig-name descname">regions</code><a class="headerlink" href="#pulumi_ns1.GetRecordResult.regions" title="Permalink to this definition"></a></dt>
<dd><p>List of regions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetRecordResult.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_ns1.GetRecordResult.ttl" title="Permalink to this definition"></a></dt>
<dd><p>The records’ time to live (in seconds).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetRecordResult.use_client_subnet">
<em class="property">property </em><code class="sig-name descname">use_client_subnet</code><a class="headerlink" href="#pulumi_ns1.GetRecordResult.use_client_subnet" title="Permalink to this definition"></a></dt>
<dd><p>Whether to use EDNS client subnet data when available (in filter chain).</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.GetZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">GetZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">additional_primaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostmaster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nx_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.GetZoneResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getZone.</p>
<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.additional_primaries">
<em class="property">property </em><code class="sig-name descname">additional_primaries</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.additional_primaries" title="Permalink to this definition"></a></dt>
<dd><p>List of additional IPv4 addresses for the primary
zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.dns_servers">
<em class="property">property </em><code class="sig-name descname">dns_servers</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.dns_servers" title="Permalink to this definition"></a></dt>
<dd><p>Authoritative Name Servers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.dnssec">
<em class="property">property </em><code class="sig-name descname">dnssec</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.dnssec" title="Permalink to this definition"></a></dt>
<dd><p>Whether or not DNSSEC is enabled for the zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.expiry">
<em class="property">property </em><code class="sig-name descname">expiry</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.expiry" title="Permalink to this definition"></a></dt>
<dd><p>The SOA Expiry.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.hostmaster">
<em class="property">property </em><code class="sig-name descname">hostmaster</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.hostmaster" title="Permalink to this definition"></a></dt>
<dd><p>The SOA Hostmaster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.link">
<em class="property">property </em><code class="sig-name descname">link</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.link" title="Permalink to this definition"></a></dt>
<dd><p>The linked target zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.networks">
<em class="property">property </em><code class="sig-name descname">networks</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.networks" title="Permalink to this definition"></a></dt>
<dd><p>List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone should be made
available. Default is network 0, the primary NSONE Global Network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.nx_ttl">
<em class="property">property </em><code class="sig-name descname">nx_ttl</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.nx_ttl" title="Permalink to this definition"></a></dt>
<dd><p>The SOA NX TTL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.primary">
<em class="property">property </em><code class="sig-name descname">primary</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.primary" title="Permalink to this definition"></a></dt>
<dd><p>The primary zones’ IPv4 address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.refresh">
<em class="property">property </em><code class="sig-name descname">refresh</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.refresh" title="Permalink to this definition"></a></dt>
<dd><p>The SOA Refresh.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.retry">
<em class="property">property </em><code class="sig-name descname">retry</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.retry" title="Permalink to this definition"></a></dt>
<dd><p>The SOA Retry.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.secondaries">
<em class="property">property </em><code class="sig-name descname">secondaries</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.secondaries" title="Permalink to this definition"></a></dt>
<dd><p>List of secondary servers. Secondaries is
documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.GetZoneResult.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_ns1.GetZoneResult.ttl" title="Permalink to this definition"></a></dt>
<dd><p>The SOA TTL.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.MonitoringJob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">MonitoringJob</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_delay</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_failback</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_list</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_regional</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_repeat</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rapid_recheck</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MonitoringJobRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MonitoringJobRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MonitoringJobRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MonitoringJobRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.MonitoringJob" title="Permalink to this definition"></a></dt>
<dd><p>Provides a NS1 Monitoring Job resource. This can be used to create, modify, and delete monitoring jobs.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_ns1</span> <span class="k">as</span> <span class="nn">ns1</span>

<span class="n">uswest_monitor</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">MonitoringJob</span><span class="p">(</span><span class="s2">&quot;uswestMonitor&quot;</span><span class="p">,</span>
    <span class="n">active</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;host&quot;</span><span class="p">:</span> <span class="s2">&quot;example-elb-uswest.aws.amazon.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">443</span><span class="p">,</span>
        <span class="s2">&quot;send&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;&quot;HEAD / HTTP/1.0</span>


<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ssl&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">frequency</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">job_type</span><span class="o">=</span><span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;quorum&quot;</span><span class="p">,</span>
    <span class="n">rapid_recheck</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">regions</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;sjc&quot;</span><span class="p">,</span>
        <span class="s2">&quot;sin&quot;</span><span class="p">,</span>
        <span class="s2">&quot;lga&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">ns1</span><span class="o">.</span><span class="n">MonitoringJobRuleArgs</span><span class="p">(</span>
        <span class="n">comparison</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
        <span class="n">key</span><span class="o">=</span><span class="s2">&quot;output&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;200 OK&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<p><a class="reference external" href="https://ns1.com/api#monitoring-jobs">MonitoringJob Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if the job is active or temporarily disabled.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A configuration dictionary with keys and values depending on the job_type. Configuration details for each job_type are found by submitting a GET request to <a class="reference external" href="https://api.nsone.net/v1/monitoring/jobtypes">https://api.nsone.net/v1/monitoring/jobtypes</a>.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The frequency, in seconds, at which to run the monitoring job in each region.</p></li>
<li><p><strong>job_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of monitoring job to be run. Refer to the NS1 API documentation (<a class="reference external" href="https://ns1.com/api#monitoring-jobs">https://ns1.com/api#monitoring-jobs</a>) for supported values which include ping, tcp, dns, http.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free-form display name for the monitoring job.</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Freeform notes to be included in any notifications about this job.</p></li>
<li><p><strong>notify_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time in seconds after a failure to wait before sending a notification.</p></li>
<li><p><strong>notify_failback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a notification is sent when a job returns to an “up” state.</p></li>
<li><p><strong>notify_regional</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, notifications are sent for any regional failure (and failback if desired), in addition to global state notifications.</p></li>
<li><p><strong>notify_repeat</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time in seconds between repeat notifications of a failed job.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy for determining the monitor’s global status
based on the status of the job in all regions. See NS1 API docs for supported values.</p></li>
<li><p><strong>rapid_recheck</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, on any apparent state change, the job is quickly re-run after one second to confirm the state change before notification.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of region codes in which to run the monitoring
job. See NS1 API docs for supported values.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitoringJobRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of rules for determining failure conditions. Each rule acts on one of the outputs from the monitoring job. You must specify key (the output key); comparison (a comparison to perform on the the output); and value (the value to compare to). For example, {“key”:”rtt”, “comparison”:”&lt;”, “value”:100} is a rule requiring the rtt from a job to be under 100ms, or the job will be marked failed. Available output keys, comparators, and value types are are found by submitting a GET request to <a class="reference external" href="https://api.nsone.net/v1/monitoring/jobtypes">https://api.nsone.net/v1/monitoring/jobtypes</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_delay</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_failback</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_list</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_regional</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_repeat</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rapid_recheck</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MonitoringJobRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MonitoringJobRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MonitoringJobRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MonitoringJobRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.MonitoringJob" title="pulumi_ns1.MonitoringJob">MonitoringJob</a><a class="headerlink" href="#pulumi_ns1.MonitoringJob.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing MonitoringJob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if the job is active or temporarily disabled.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A configuration dictionary with keys and values depending on the job_type. Configuration details for each job_type are found by submitting a GET request to <a class="reference external" href="https://api.nsone.net/v1/monitoring/jobtypes">https://api.nsone.net/v1/monitoring/jobtypes</a>.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The frequency, in seconds, at which to run the monitoring job in each region.</p></li>
<li><p><strong>job_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of monitoring job to be run. Refer to the NS1 API documentation (<a class="reference external" href="https://ns1.com/api#monitoring-jobs">https://ns1.com/api#monitoring-jobs</a>) for supported values which include ping, tcp, dns, http.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free-form display name for the monitoring job.</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Freeform notes to be included in any notifications about this job.</p></li>
<li><p><strong>notify_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time in seconds after a failure to wait before sending a notification.</p></li>
<li><p><strong>notify_failback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a notification is sent when a job returns to an “up” state.</p></li>
<li><p><strong>notify_regional</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, notifications are sent for any regional failure (and failback if desired), in addition to global state notifications.</p></li>
<li><p><strong>notify_repeat</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time in seconds between repeat notifications of a failed job.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy for determining the monitor’s global status
based on the status of the job in all regions. See NS1 API docs for supported values.</p></li>
<li><p><strong>rapid_recheck</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, on any apparent state change, the job is quickly re-run after one second to confirm the state change before notification.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of region codes in which to run the monitoring
job. See NS1 API docs for supported values.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitoringJobRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of rules for determining failure conditions. Each rule acts on one of the outputs from the monitoring job. You must specify key (the output key); comparison (a comparison to perform on the the output); and value (the value to compare to). For example, {“key”:”rtt”, “comparison”:”&lt;”, “value”:100} is a rule requiring the rtt from a job to be under 100ms, or the job will be marked failed. Available output keys, comparators, and value types are are found by submitting a GET request to <a class="reference external" href="https://api.nsone.net/v1/monitoring/jobtypes">https://api.nsone.net/v1/monitoring/jobtypes</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.active">
<em class="property">property </em><code class="sig-name descname">active</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.active" title="Permalink to this definition"></a></dt>
<dd><p>Indicates if the job is active or temporarily disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.config" title="Permalink to this definition"></a></dt>
<dd><p>A configuration dictionary with keys and values depending on the job_type. Configuration details for each job_type are found by submitting a GET request to <a class="reference external" href="https://api.nsone.net/v1/monitoring/jobtypes">https://api.nsone.net/v1/monitoring/jobtypes</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.frequency">
<em class="property">property </em><code class="sig-name descname">frequency</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.frequency" title="Permalink to this definition"></a></dt>
<dd><p>The frequency, in seconds, at which to run the monitoring job in each region.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.job_type">
<em class="property">property </em><code class="sig-name descname">job_type</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.job_type" title="Permalink to this definition"></a></dt>
<dd><p>The type of monitoring job to be run. Refer to the NS1 API documentation (<a class="reference external" href="https://ns1.com/api#monitoring-jobs">https://ns1.com/api#monitoring-jobs</a>) for supported values which include ping, tcp, dns, http.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.name" title="Permalink to this definition"></a></dt>
<dd><p>The free-form display name for the monitoring job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.notes">
<em class="property">property </em><code class="sig-name descname">notes</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notes" title="Permalink to this definition"></a></dt>
<dd><p>Freeform notes to be included in any notifications about this job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.notify_delay">
<em class="property">property </em><code class="sig-name descname">notify_delay</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_delay" title="Permalink to this definition"></a></dt>
<dd><p>The time in seconds after a failure to wait before sending a notification.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.notify_failback">
<em class="property">property </em><code class="sig-name descname">notify_failback</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_failback" title="Permalink to this definition"></a></dt>
<dd><p>If true, a notification is sent when a job returns to an “up” state.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.notify_regional">
<em class="property">property </em><code class="sig-name descname">notify_regional</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_regional" title="Permalink to this definition"></a></dt>
<dd><p>If true, notifications are sent for any regional failure (and failback if desired), in addition to global state notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.notify_repeat">
<em class="property">property </em><code class="sig-name descname">notify_repeat</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_repeat" title="Permalink to this definition"></a></dt>
<dd><p>The time in seconds between repeat notifications of a failed job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.policy">
<em class="property">property </em><code class="sig-name descname">policy</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.policy" title="Permalink to this definition"></a></dt>
<dd><p>The policy for determining the monitor’s global status
based on the status of the job in all regions. See NS1 API docs for supported values.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.rapid_recheck">
<em class="property">property </em><code class="sig-name descname">rapid_recheck</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.rapid_recheck" title="Permalink to this definition"></a></dt>
<dd><p>If true, on any apparent state change, the job is quickly re-run after one second to confirm the state change before notification.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.regions">
<em class="property">property </em><code class="sig-name descname">regions</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.regions" title="Permalink to this definition"></a></dt>
<dd><p>The list of region codes in which to run the monitoring
job. See NS1 API docs for supported values.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_ns1.MonitoringJob.rules" title="Permalink to this definition"></a></dt>
<dd><p>A list of rules for determining failure conditions. Each rule acts on one of the outputs from the monitoring job. You must specify key (the output key); comparison (a comparison to perform on the the output); and value (the value to compare to). For example, {“key”:”rtt”, “comparison”:”&lt;”, “value”:100} is a rule requiring the rtt from a job to be under 100ms, or the job will be marked failed. Available output keys, comparators, and value types are are found by submitting a GET request to <a class="reference external" href="https://api.nsone.net/v1/monitoring/jobtypes">https://api.nsone.net/v1/monitoring/jobtypes</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.MonitoringJob.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.MonitoringJob.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">NotifyList</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotifyListNotificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotifyListNotificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotifyListNotificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotifyListNotificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.NotifyList" title="Permalink to this definition"></a></dt>
<dd><p>Provides a NS1 Notify List resource. This can be used to create, modify, and delete notify lists.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_ns1</span> <span class="k">as</span> <span class="nn">ns1</span>

<span class="n">nl</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">NotifyList</span><span class="p">(</span><span class="s2">&quot;nl&quot;</span><span class="p">,</span> <span class="n">notifications</span><span class="o">=</span><span class="p">[</span>
    <span class="n">ns1</span><span class="o">.</span><span class="n">NotifyListNotificationArgs</span><span class="p">(</span>
        <span class="n">config</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;http://www.mywebhook.com&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;webhook&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">ns1</span><span class="o">.</span><span class="n">NotifyListNotificationArgs</span><span class="p">(</span>
        <span class="n">config</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;email&quot;</span><span class="p">:</span> <span class="s2">&quot;test@test.com&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="p">),</span>
<span class="p">])</span>
</pre></div>
</div>
<p><a class="reference external" href="https://ns1.com/api#notification-lists">NotifyList Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free-form display name for the notify list.</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotifyListNotificationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of notifiers. All notifiers in a notification list will receive notifications whenever an event is send to the list (e.g., when a monitoring job fails). Notifiers are documented below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_ns1.NotifyList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotifyListNotificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotifyListNotificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotifyListNotificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotifyListNotificationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.NotifyList" title="pulumi_ns1.NotifyList">NotifyList</a><a class="headerlink" href="#pulumi_ns1.NotifyList.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing NotifyList resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free-form display name for the notify list.</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotifyListNotificationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of notifiers. All notifiers in a notification list will receive notifications whenever an event is send to the list (e.g., when a monitoring job fails). Notifiers are documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.NotifyList.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_ns1.NotifyList.name" title="Permalink to this definition"></a></dt>
<dd><p>The free-form display name for the notify list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.NotifyList.notifications">
<em class="property">property </em><code class="sig-name descname">notifications</code><a class="headerlink" href="#pulumi_ns1.NotifyList.notifications" title="Permalink to this definition"></a></dt>
<dd><p>A list of notifiers. All notifiers in a notification list will receive notifications whenever an event is send to the list (e.g., when a monitoring job fails). Notifiers are documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.NotifyList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.NotifyList.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.NotifyList.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apikey</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ddi</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_ssl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate_limit_parallelism</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Provider" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Provider.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Provider.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">Record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">answers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordAnswerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordAnswerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordAnswerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordAnswerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordRegionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordRegionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordRegionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordRegionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_answers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_client_subnet</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Record" title="Permalink to this definition"></a></dt>
<dd><p>Provides a NS1 Record resource. This can be used to create, modify, and delete records.</p>
<p><a class="reference external" href="https://ns1.com/api#records">Record Api Doc</a></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import ns1:index/record:Record &lt;name&gt; &lt;zone&gt;/&lt;domain&gt;/&lt;type&gt;<span class="sb">`</span>

So <span class="k">for</span> the example above
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import ns1:index/record:Record www terraform.example.io/www.terraform.example.io/CNAME<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>answers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RecordAnswerArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – One or more NS1 answers for the records’ specified type.
Answers are documented below.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The records’ domain. Cannot have leading or trailing
dots - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RecordFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – One or more NS1 filters for the record(order matters).
Filters are documented below.</p></li>
<li><p><strong>link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target record to link to. This means this record is a
‘linked’ record, and it inherits all properties from its target.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RecordRegionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – One or more “regions” for the record. These are really
just groupings based on metadata, and are called “Answer Groups” in the NS1 UI,
but remain <code class="docutils literal notranslate"><span class="pre">regions</span></code> here for legacy reasons. Regions are
documented below. Please note the ordering requirement!</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The records’ time to live (in seconds).</p></li>
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
<dl class="py method">
<dt id="pulumi_ns1.Record.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">answers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordAnswerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordAnswerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordAnswerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordAnswerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordRegionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordRegionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>RecordRegionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>RecordRegionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_answers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_client_subnet</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.Record" title="pulumi_ns1.Record">Record</a><a class="headerlink" href="#pulumi_ns1.Record.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>answers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RecordAnswerArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – One or more NS1 answers for the records’ specified type.
Answers are documented below.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The records’ domain. Cannot have leading or trailing
dots - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RecordFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – One or more NS1 filters for the record(order matters).
Filters are documented below.</p></li>
<li><p><strong>link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target record to link to. This means this record is a
‘linked’ record, and it inherits all properties from its target.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RecordRegionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – One or more “regions” for the record. These are really
just groupings based on metadata, and are called “Answer Groups” in the NS1 UI,
but remain <code class="docutils literal notranslate"><span class="pre">regions</span></code> here for legacy reasons. Regions are
documented below. Please note the ordering requirement!</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The records’ time to live (in seconds).</p></li>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.answers">
<em class="property">property </em><code class="sig-name descname">answers</code><a class="headerlink" href="#pulumi_ns1.Record.answers" title="Permalink to this definition"></a></dt>
<dd><p>One or more NS1 answers for the records’ specified type.
Answers are documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_ns1.Record.domain" title="Permalink to this definition"></a></dt>
<dd><p>The records’ domain. Cannot have leading or trailing
dots - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.filters">
<em class="property">property </em><code class="sig-name descname">filters</code><a class="headerlink" href="#pulumi_ns1.Record.filters" title="Permalink to this definition"></a></dt>
<dd><p>One or more NS1 filters for the record(order matters).
Filters are documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.link">
<em class="property">property </em><code class="sig-name descname">link</code><a class="headerlink" href="#pulumi_ns1.Record.link" title="Permalink to this definition"></a></dt>
<dd><p>The target record to link to. This means this record is a
‘linked’ record, and it inherits all properties from its target.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.regions">
<em class="property">property </em><code class="sig-name descname">regions</code><a class="headerlink" href="#pulumi_ns1.Record.regions" title="Permalink to this definition"></a></dt>
<dd><p>One or more “regions” for the record. These are really
just groupings based on metadata, and are called “Answer Groups” in the NS1 UI,
but remain <code class="docutils literal notranslate"><span class="pre">regions</span></code> here for legacy reasons. Regions are
documented below. Please note the ordering requirement!</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_ns1.Record.ttl" title="Permalink to this definition"></a></dt>
<dd><p>The records’ time to live (in seconds).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_ns1.Record.type" title="Permalink to this definition"></a></dt>
<dd><p>The records’ RR type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.use_client_subnet">
<em class="property">property </em><code class="sig-name descname">use_client_subnet</code><a class="headerlink" href="#pulumi_ns1.Record.use_client_subnet" title="Permalink to this definition"></a></dt>
<dd><p>Whether to use EDNS client subnet data when
available(in filter chain).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> - (Optional) meta is supported at the <code class="docutils literal notranslate"><span class="pre">record</span></code> level. Meta
is documented below.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.zone">
<em class="property">property </em><code class="sig-name descname">zone</code><a class="headerlink" href="#pulumi_ns1.Record.zone" title="Permalink to this definition"></a></dt>
<dd><p>The zone the record belongs to. Cannot have leading or
trailing dots (“.”) - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Record.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Record.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamIpWhitelistArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamIpWhitelistArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamIpWhitelistArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamIpWhitelistArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Team" title="Permalink to this definition"></a></dt>
<dd><p>Provides a NS1 Team resource. This can be used to create, modify, and delete
teams. The credentials used must have the <code class="docutils literal notranslate"><span class="pre">manage_teams</span></code> permission set.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_ns1</span> <span class="k">as</span> <span class="nn">ns1</span>

<span class="c1"># Create a new NS1 Team</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">account_manage_users</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">dns_view_zones</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">ip_whitelists</span><span class="o">=</span><span class="p">[</span>
        <span class="n">ns1</span><span class="o">.</span><span class="n">TeamIpWhitelistArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;whitelist-1&quot;</span><span class="p">,</span>
            <span class="n">values</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;1.1.1.1&quot;</span><span class="p">,</span>
                <span class="s2">&quot;2.2.2.2&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">),</span>
        <span class="n">ns1</span><span class="o">.</span><span class="n">TeamIpWhitelistArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;whitelist-2&quot;</span><span class="p">,</span>
            <span class="n">values</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;3.3.3.3&quot;</span><span class="p">,</span>
                <span class="s2">&quot;4.4.4.4&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">),</span>
    <span class="p">])</span>
<span class="c1"># Another team</span>
<span class="n">example2</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;example2&quot;</span><span class="p">,</span>
    <span class="n">data_manage_datasources</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">dns_view_zones</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">dns_zones_allows</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;mytest.zone&quot;</span><span class="p">],</span>
    <span class="n">dns_zones_allow_by_default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">dns_zones_denies</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;myother.zone&quot;</span><span class="p">])</span>
</pre></div>
</div>
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
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the team may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the team may not access.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TeamIpWhitelistArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
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
<dl class="py method">
<dt id="pulumi_ns1.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamIpWhitelistArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamIpWhitelistArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamIpWhitelistArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamIpWhitelistArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.Team" title="pulumi_ns1.Team">Team</a><a class="headerlink" href="#pulumi_ns1.Team.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the team may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the team may not access.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TeamIpWhitelistArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.account_manage_account_settings">
<em class="property">property </em><code class="sig-name descname">account_manage_account_settings</code><a class="headerlink" href="#pulumi_ns1.Team.account_manage_account_settings" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify account settings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.account_manage_apikeys">
<em class="property">property </em><code class="sig-name descname">account_manage_apikeys</code><a class="headerlink" href="#pulumi_ns1.Team.account_manage_apikeys" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify account apikeys.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.account_manage_payment_methods">
<em class="property">property </em><code class="sig-name descname">account_manage_payment_methods</code><a class="headerlink" href="#pulumi_ns1.Team.account_manage_payment_methods" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify account payment methods.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.account_manage_plan">
<em class="property">property </em><code class="sig-name descname">account_manage_plan</code><a class="headerlink" href="#pulumi_ns1.Team.account_manage_plan" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify the account plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.account_manage_teams">
<em class="property">property </em><code class="sig-name descname">account_manage_teams</code><a class="headerlink" href="#pulumi_ns1.Team.account_manage_teams" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify other teams in the account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.account_manage_users">
<em class="property">property </em><code class="sig-name descname">account_manage_users</code><a class="headerlink" href="#pulumi_ns1.Team.account_manage_users" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify account users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.account_view_activity_log">
<em class="property">property </em><code class="sig-name descname">account_view_activity_log</code><a class="headerlink" href="#pulumi_ns1.Team.account_view_activity_log" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can view activity logs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.account_view_invoices">
<em class="property">property </em><code class="sig-name descname">account_view_invoices</code><a class="headerlink" href="#pulumi_ns1.Team.account_view_invoices" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can view invoices.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.data_manage_datafeeds">
<em class="property">property </em><code class="sig-name descname">data_manage_datafeeds</code><a class="headerlink" href="#pulumi_ns1.Team.data_manage_datafeeds" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify data feeds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.data_manage_datasources">
<em class="property">property </em><code class="sig-name descname">data_manage_datasources</code><a class="headerlink" href="#pulumi_ns1.Team.data_manage_datasources" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify data sources.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.data_push_to_datafeeds">
<em class="property">property </em><code class="sig-name descname">data_push_to_datafeeds</code><a class="headerlink" href="#pulumi_ns1.Team.data_push_to_datafeeds" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can publish to data feeds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.dhcp_manage_dhcp">
<em class="property">property </em><code class="sig-name descname">dhcp_manage_dhcp</code><a class="headerlink" href="#pulumi_ns1.Team.dhcp_manage_dhcp" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can manage DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.dhcp_view_dhcp">
<em class="property">property </em><code class="sig-name descname">dhcp_view_dhcp</code><a class="headerlink" href="#pulumi_ns1.Team.dhcp_view_dhcp" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can view DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.dns_manage_zones">
<em class="property">property </em><code class="sig-name descname">dns_manage_zones</code><a class="headerlink" href="#pulumi_ns1.Team.dns_manage_zones" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify the accounts zones.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.dns_view_zones">
<em class="property">property </em><code class="sig-name descname">dns_view_zones</code><a class="headerlink" href="#pulumi_ns1.Team.dns_view_zones" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can view the accounts zones.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.dns_zones_allow_by_default">
<em class="property">property </em><code class="sig-name descname">dns_zones_allow_by_default</code><a class="headerlink" href="#pulumi_ns1.Team.dns_zones_allow_by_default" title="Permalink to this definition"></a></dt>
<dd><p>If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.dns_zones_allows">
<em class="property">property </em><code class="sig-name descname">dns_zones_allows</code><a class="headerlink" href="#pulumi_ns1.Team.dns_zones_allows" title="Permalink to this definition"></a></dt>
<dd><p>List of zones that the team may access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.dns_zones_denies">
<em class="property">property </em><code class="sig-name descname">dns_zones_denies</code><a class="headerlink" href="#pulumi_ns1.Team.dns_zones_denies" title="Permalink to this definition"></a></dt>
<dd><p>List of zones that the team may not access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.ip_whitelists">
<em class="property">property </em><code class="sig-name descname">ip_whitelists</code><a class="headerlink" href="#pulumi_ns1.Team.ip_whitelists" title="Permalink to this definition"></a></dt>
<dd><p>The IP addresses to whitelist for this key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.ipam_manage_ipam">
<em class="property">property </em><code class="sig-name descname">ipam_manage_ipam</code><a class="headerlink" href="#pulumi_ns1.Team.ipam_manage_ipam" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can manage IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.ipam_view_ipam">
<em class="property">property </em><code class="sig-name descname">ipam_view_ipam</code><a class="headerlink" href="#pulumi_ns1.Team.ipam_view_ipam" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can view IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.monitoring_manage_jobs">
<em class="property">property </em><code class="sig-name descname">monitoring_manage_jobs</code><a class="headerlink" href="#pulumi_ns1.Team.monitoring_manage_jobs" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify monitoring jobs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.monitoring_manage_lists">
<em class="property">property </em><code class="sig-name descname">monitoring_manage_lists</code><a class="headerlink" href="#pulumi_ns1.Team.monitoring_manage_lists" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can modify notification lists.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.monitoring_view_jobs">
<em class="property">property </em><code class="sig-name descname">monitoring_view_jobs</code><a class="headerlink" href="#pulumi_ns1.Team.monitoring_view_jobs" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can view monitoring jobs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_ns1.Team.name" title="Permalink to this definition"></a></dt>
<dd><p>The free form name of the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.security_manage_active_directory">
<em class="property">property </em><code class="sig-name descname">security_manage_active_directory</code><a class="headerlink" href="#pulumi_ns1.Team.security_manage_active_directory" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can manage global active directory.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.security_manage_global2fa">
<em class="property">property </em><code class="sig-name descname">security_manage_global2fa</code><a class="headerlink" href="#pulumi_ns1.Team.security_manage_global2fa" title="Permalink to this definition"></a></dt>
<dd><p>Whether the team can manage global two factor authentication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Team.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Team.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_strict</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.User" title="Permalink to this definition"></a></dt>
<dd><p>Create a User resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] account_manage_account_settings: Whether the user can modify account settings.
:param pulumi.Input[bool] account_manage_apikeys: Whether the user can modify account apikeys.
:param pulumi.Input[bool] account_manage_payment_methods: Whether the user can modify account payment methods.
:param pulumi.Input[bool] account_manage_plan: <strong>Deprecated</strong> Whether the user can modify the account plan.
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
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the user may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the user may not access.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user.</p></li>
<li><p><strong>ip_whitelist_strict</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets exclusivity on this IP whitelist.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
<li><p><strong>ipam_manage_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>monitoring_manage_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify monitoring jobs.</p></li>
<li><p><strong>monitoring_manage_lists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify notification lists.</p></li>
<li><p><strong>monitoring_view_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view monitoring jobs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the user.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>notify</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Whether or not to notify the user of specified events. Only <code class="docutils literal notranslate"><span class="pre">billing</span></code> is available currently.</p></li>
<li><p><strong>security_manage_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage global active directory.
Only relevant for the DDI product.</p></li>
<li><p><strong>security_manage_global2fa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage global two factor authentication.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The teams that the user belongs to.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users login name.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_ns1.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_strict</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.User" title="pulumi_ns1.User">User</a><a class="headerlink" href="#pulumi_ns1.User.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_manage_account_settings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify account settings.</p></li>
<li><p><strong>account_manage_apikeys</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify account apikeys.</p></li>
<li><p><strong>account_manage_payment_methods</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify account payment methods.</p></li>
<li><p><strong>account_manage_plan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <strong>Deprecated</strong> Whether the user can modify the account plan.</p></li>
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
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the user may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of zones that the user may not access.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user.</p></li>
<li><p><strong>ip_whitelist_strict</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets exclusivity on this IP whitelist.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
<li><p><strong>ipam_manage_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>monitoring_manage_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify monitoring jobs.</p></li>
<li><p><strong>monitoring_manage_lists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify notification lists.</p></li>
<li><p><strong>monitoring_view_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view monitoring jobs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the user.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>notify</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Whether or not to notify the user of specified events. Only <code class="docutils literal notranslate"><span class="pre">billing</span></code> is available currently.</p></li>
<li><p><strong>security_manage_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage global active directory.
Only relevant for the DDI product.</p></li>
<li><p><strong>security_manage_global2fa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage global two factor authentication.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The teams that the user belongs to.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users login name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.account_manage_account_settings">
<em class="property">property </em><code class="sig-name descname">account_manage_account_settings</code><a class="headerlink" href="#pulumi_ns1.User.account_manage_account_settings" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify account settings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.account_manage_apikeys">
<em class="property">property </em><code class="sig-name descname">account_manage_apikeys</code><a class="headerlink" href="#pulumi_ns1.User.account_manage_apikeys" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify account apikeys.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.account_manage_payment_methods">
<em class="property">property </em><code class="sig-name descname">account_manage_payment_methods</code><a class="headerlink" href="#pulumi_ns1.User.account_manage_payment_methods" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify account payment methods.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.account_manage_plan">
<em class="property">property </em><code class="sig-name descname">account_manage_plan</code><a class="headerlink" href="#pulumi_ns1.User.account_manage_plan" title="Permalink to this definition"></a></dt>
<dd><p><strong>Deprecated</strong> Whether the user can modify the account plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.account_manage_teams">
<em class="property">property </em><code class="sig-name descname">account_manage_teams</code><a class="headerlink" href="#pulumi_ns1.User.account_manage_teams" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify other teams in the account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.account_manage_users">
<em class="property">property </em><code class="sig-name descname">account_manage_users</code><a class="headerlink" href="#pulumi_ns1.User.account_manage_users" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify account users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.account_view_activity_log">
<em class="property">property </em><code class="sig-name descname">account_view_activity_log</code><a class="headerlink" href="#pulumi_ns1.User.account_view_activity_log" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can view activity logs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.account_view_invoices">
<em class="property">property </em><code class="sig-name descname">account_view_invoices</code><a class="headerlink" href="#pulumi_ns1.User.account_view_invoices" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can view invoices.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.data_manage_datafeeds">
<em class="property">property </em><code class="sig-name descname">data_manage_datafeeds</code><a class="headerlink" href="#pulumi_ns1.User.data_manage_datafeeds" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify data feeds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.data_manage_datasources">
<em class="property">property </em><code class="sig-name descname">data_manage_datasources</code><a class="headerlink" href="#pulumi_ns1.User.data_manage_datasources" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify data sources.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.data_push_to_datafeeds">
<em class="property">property </em><code class="sig-name descname">data_push_to_datafeeds</code><a class="headerlink" href="#pulumi_ns1.User.data_push_to_datafeeds" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can publish to data feeds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.dhcp_manage_dhcp">
<em class="property">property </em><code class="sig-name descname">dhcp_manage_dhcp</code><a class="headerlink" href="#pulumi_ns1.User.dhcp_manage_dhcp" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can manage DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.dhcp_view_dhcp">
<em class="property">property </em><code class="sig-name descname">dhcp_view_dhcp</code><a class="headerlink" href="#pulumi_ns1.User.dhcp_view_dhcp" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can view DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.dns_manage_zones">
<em class="property">property </em><code class="sig-name descname">dns_manage_zones</code><a class="headerlink" href="#pulumi_ns1.User.dns_manage_zones" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify the accounts zones.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.dns_view_zones">
<em class="property">property </em><code class="sig-name descname">dns_view_zones</code><a class="headerlink" href="#pulumi_ns1.User.dns_view_zones" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can view the accounts zones.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.dns_zones_allow_by_default">
<em class="property">property </em><code class="sig-name descname">dns_zones_allow_by_default</code><a class="headerlink" href="#pulumi_ns1.User.dns_zones_allow_by_default" title="Permalink to this definition"></a></dt>
<dd><p>If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.dns_zones_allows">
<em class="property">property </em><code class="sig-name descname">dns_zones_allows</code><a class="headerlink" href="#pulumi_ns1.User.dns_zones_allows" title="Permalink to this definition"></a></dt>
<dd><p>List of zones that the user may access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.dns_zones_denies">
<em class="property">property </em><code class="sig-name descname">dns_zones_denies</code><a class="headerlink" href="#pulumi_ns1.User.dns_zones_denies" title="Permalink to this definition"></a></dt>
<dd><p>List of zones that the user may not access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_ns1.User.email" title="Permalink to this definition"></a></dt>
<dd><p>The email address of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.ip_whitelist_strict">
<em class="property">property </em><code class="sig-name descname">ip_whitelist_strict</code><a class="headerlink" href="#pulumi_ns1.User.ip_whitelist_strict" title="Permalink to this definition"></a></dt>
<dd><p>Sets exclusivity on this IP whitelist.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.ip_whitelists">
<em class="property">property </em><code class="sig-name descname">ip_whitelists</code><a class="headerlink" href="#pulumi_ns1.User.ip_whitelists" title="Permalink to this definition"></a></dt>
<dd><p>The IP addresses to whitelist for this key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.ipam_manage_ipam">
<em class="property">property </em><code class="sig-name descname">ipam_manage_ipam</code><a class="headerlink" href="#pulumi_ns1.User.ipam_manage_ipam" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can manage IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.monitoring_manage_jobs">
<em class="property">property </em><code class="sig-name descname">monitoring_manage_jobs</code><a class="headerlink" href="#pulumi_ns1.User.monitoring_manage_jobs" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify monitoring jobs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.monitoring_manage_lists">
<em class="property">property </em><code class="sig-name descname">monitoring_manage_lists</code><a class="headerlink" href="#pulumi_ns1.User.monitoring_manage_lists" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can modify notification lists.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.monitoring_view_jobs">
<em class="property">property </em><code class="sig-name descname">monitoring_view_jobs</code><a class="headerlink" href="#pulumi_ns1.User.monitoring_view_jobs" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can view monitoring jobs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_ns1.User.name" title="Permalink to this definition"></a></dt>
<dd><p>The free form name of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.notify">
<em class="property">property </em><code class="sig-name descname">notify</code><a class="headerlink" href="#pulumi_ns1.User.notify" title="Permalink to this definition"></a></dt>
<dd><p>Whether or not to notify the user of specified events. Only <code class="docutils literal notranslate"><span class="pre">billing</span></code> is available currently.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.security_manage_active_directory">
<em class="property">property </em><code class="sig-name descname">security_manage_active_directory</code><a class="headerlink" href="#pulumi_ns1.User.security_manage_active_directory" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can manage global active directory.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.security_manage_global2fa">
<em class="property">property </em><code class="sig-name descname">security_manage_global2fa</code><a class="headerlink" href="#pulumi_ns1.User.security_manage_global2fa" title="Permalink to this definition"></a></dt>
<dd><p>Whether the user can manage global two factor authentication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.teams">
<em class="property">property </em><code class="sig-name descname">teams</code><a class="headerlink" href="#pulumi_ns1.User.teams" title="Permalink to this definition"></a></dt>
<dd><p>The teams that the user belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_ns1.User.username" title="Permalink to this definition"></a></dt>
<dd><p>The users login name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.User.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.User.translate_input_property" title="Permalink to this definition"></a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_primaries</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autogenerate_ns_record</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nx_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondaries</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ZoneSecondaryArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ZoneSecondaryArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ZoneSecondaryArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ZoneSecondaryArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Zone" title="Permalink to this definition"></a></dt>
<dd><div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import ns1:index/zone:Zone &lt;name&gt; &lt;zone&gt;<span class="sb">`</span>

So <span class="k">for</span> the example above
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import ns1:index/zone:Zone example terraform.example.io<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_primaries</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of additional IPv4 addresses for the primary
zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p></li>
<li><p><strong>dnssec</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not DNSSEC is enabled for the zone.
Note that DNSSEC must be enabled on the account by support for this to be set
to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA Expiry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target zone(domain name) to link to.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p>List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone</p></li>
</ul>
<p>should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p>
</p></li>
<li><p><strong>nx_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA NX TTL. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>primary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary zones’ IPv4 address. This makes the zone a
secondary. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p></li>
<li><p><strong>refresh</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA Refresh. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>retry</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA Retry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>secondaries</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ZoneSecondaryArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of secondary servers. This makes the zone a
primary. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and <code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code>.
Secondaries is documented below.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA TTL.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name of the zone.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_ns1.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_primaries</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autogenerate_ns_record</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_servers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostmaster</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nx_ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondaries</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ZoneSecondaryArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ZoneSecondaryArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ZoneSecondaryArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ZoneSecondaryArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_ns1.Zone" title="pulumi_ns1.Zone">Zone</a><a class="headerlink" href="#pulumi_ns1.Zone.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_primaries</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of additional IPv4 addresses for the primary
zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) Authoritative Name Servers.</p></li>
<li><p><strong>dnssec</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not DNSSEC is enabled for the zone.
Note that DNSSEC must be enabled on the account by support for this to be set
to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA Expiry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>hostmaster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The SOA Hostmaster.</p></li>
<li><p><strong>link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target zone(domain name) to link to.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p>List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone</p></li>
</ul>
<p>should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p>
</p></li>
<li><p><strong>nx_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA NX TTL. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>primary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary zones’ IPv4 address. This makes the zone a
secondary. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p></li>
<li><p><strong>refresh</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA Refresh. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>retry</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA Retry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>secondaries</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ZoneSecondaryArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of secondary servers. This makes the zone a
primary. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and <code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code>.
Secondaries is documented below.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The SOA TTL.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name of the zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.additional_primaries">
<em class="property">property </em><code class="sig-name descname">additional_primaries</code><a class="headerlink" href="#pulumi_ns1.Zone.additional_primaries" title="Permalink to this definition"></a></dt>
<dd><p>List of additional IPv4 addresses for the primary
zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.dns_servers">
<em class="property">property </em><code class="sig-name descname">dns_servers</code><a class="headerlink" href="#pulumi_ns1.Zone.dns_servers" title="Permalink to this definition"></a></dt>
<dd><p>(Computed) Authoritative Name Servers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.dnssec">
<em class="property">property </em><code class="sig-name descname">dnssec</code><a class="headerlink" href="#pulumi_ns1.Zone.dnssec" title="Permalink to this definition"></a></dt>
<dd><p>Whether or not DNSSEC is enabled for the zone.
Note that DNSSEC must be enabled on the account by support for this to be set
to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.expiry">
<em class="property">property </em><code class="sig-name descname">expiry</code><a class="headerlink" href="#pulumi_ns1.Zone.expiry" title="Permalink to this definition"></a></dt>
<dd><p>The SOA Expiry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.hostmaster">
<em class="property">property </em><code class="sig-name descname">hostmaster</code><a class="headerlink" href="#pulumi_ns1.Zone.hostmaster" title="Permalink to this definition"></a></dt>
<dd><p>(Computed) The SOA Hostmaster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.link">
<em class="property">property </em><code class="sig-name descname">link</code><a class="headerlink" href="#pulumi_ns1.Zone.link" title="Permalink to this definition"></a></dt>
<dd><p>The target zone(domain name) to link to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.networks">
<em class="property">property </em><code class="sig-name descname">networks</code><a class="headerlink" href="#pulumi_ns1.Zone.networks" title="Permalink to this definition"></a></dt>
<dd><ul class="simple">
<li><p>List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone
should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.nx_ttl">
<em class="property">property </em><code class="sig-name descname">nx_ttl</code><a class="headerlink" href="#pulumi_ns1.Zone.nx_ttl" title="Permalink to this definition"></a></dt>
<dd><p>The SOA NX TTL. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.primary">
<em class="property">property </em><code class="sig-name descname">primary</code><a class="headerlink" href="#pulumi_ns1.Zone.primary" title="Permalink to this definition"></a></dt>
<dd><p>The primary zones’ IPv4 address. This makes the zone a
secondary. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.refresh">
<em class="property">property </em><code class="sig-name descname">refresh</code><a class="headerlink" href="#pulumi_ns1.Zone.refresh" title="Permalink to this definition"></a></dt>
<dd><p>The SOA Refresh. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.retry">
<em class="property">property </em><code class="sig-name descname">retry</code><a class="headerlink" href="#pulumi_ns1.Zone.retry" title="Permalink to this definition"></a></dt>
<dd><p>The SOA Retry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.secondaries">
<em class="property">property </em><code class="sig-name descname">secondaries</code><a class="headerlink" href="#pulumi_ns1.Zone.secondaries" title="Permalink to this definition"></a></dt>
<dd><p>List of secondary servers. This makes the zone a
primary. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and <code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code>.
Secondaries is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_ns1.Zone.ttl" title="Permalink to this definition"></a></dt>
<dd><p>The SOA TTL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.zone">
<em class="property">property </em><code class="sig-name descname">zone</code><a class="headerlink" href="#pulumi_ns1.Zone.zone" title="Permalink to this definition"></a></dt>
<dd><p>The domain name of the zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Zone.translate_output_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Zone.translate_input_property" title="Permalink to this definition"></a></dt>
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
<code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">get_dns_sec</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_ns1.get_dns_sec.AwaitableGetDNSSecResult<a class="headerlink" href="#pulumi_ns1.get_dns_sec" title="Permalink to this definition"></a></dt>
<dd><p>Provides DNSSEC details about a NS1 Zone.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_ns1</span> <span class="k">as</span> <span class="nn">ns1</span>

<span class="c1"># Get DNSSEC details about a NS1 Zone.</span>
<span class="n">example_zone</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">Zone</span><span class="p">(</span><span class="s2">&quot;exampleZone&quot;</span><span class="p">,</span>
    <span class="n">dnssec</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">zone</span><span class="o">=</span><span class="s2">&quot;terraform.example.io&quot;</span><span class="p">)</span>
<span class="n">example_dns_sec</span> <span class="o">=</span> <span class="n">example_zone</span><span class="o">.</span><span class="n">zone</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">zone</span><span class="p">:</span> <span class="n">ns1</span><span class="o">.</span><span class="n">get_dns_sec</span><span class="p">(</span><span class="n">zone</span><span class="o">=</span><span class="n">zone</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>zone</strong> (<em>str</em>) – The name of the zone to get DNSSEC details for.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_ns1.get_record">
<code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">get_record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_ns1.get_record.AwaitableGetRecordResult<a class="headerlink" href="#pulumi_ns1.get_record" title="Permalink to this definition"></a></dt>
<dd><p>Provides details about a NS1 Record. Use this if you would simply like to read
information from NS1 into your configurations. For read/write operations, you
should use a resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_ns1</span> <span class="k">as</span> <span class="nn">ns1</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">get_record</span><span class="p">(</span><span class="n">domain</span><span class="o">=</span><span class="s2">&quot;terraform.example.io&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;A&quot;</span><span class="p">,</span>
    <span class="n">zone</span><span class="o">=</span><span class="s2">&quot;example.io&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>str</em>) – The records’ domain.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The records’ RR type.</p></li>
<li><p><strong>zone</strong> (<em>str</em>) – The zone the record belongs to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_ns1.get_zone">
<code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">get_zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">additional_primaries</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_ns1.get_zone.AwaitableGetZoneResult<a class="headerlink" href="#pulumi_ns1.get_zone" title="Permalink to this definition"></a></dt>
<dd><p>Provides details about a NS1 Zone. Use this if you would simply like to read
information from NS1 into your configurations. For read/write operations, you
should use a resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_ns1</span> <span class="k">as</span> <span class="nn">ns1</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ns1</span><span class="o">.</span><span class="n">get_zone</span><span class="p">(</span><span class="n">zone</span><span class="o">=</span><span class="s2">&quot;terraform.example.io&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>additional_primaries</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – List of additional IPv4 addresses for the primary
zone.</p></li>
<li><p><strong>zone</strong> (<em>str</em>) – The domain name of the zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
