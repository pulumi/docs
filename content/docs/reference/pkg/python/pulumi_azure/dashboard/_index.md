---
title: Module dashboard
title_tag: Module dashboard | Package pulumi_azure | Python SDK
linktitle: dashboard
notitle: true
---

<div class="section" id="dashboard">
<h1>dashboard<a class="headerlink" href="#dashboard" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.dashboard"></span><dl class="py class">
<dt id="pulumi_azure.dashboard.Dashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.dashboard.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a shared dashboard in the Azure Portal.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">md_content</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;mdContent&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">md_content</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">md_content</span> <span class="o">=</span> <span class="s2">&quot;# Hello all :)&quot;</span>
<span class="n">video_link</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;videoLink&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">video_link</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">video_link</span> <span class="o">=</span> <span class="s2">&quot;https://www.youtube.com/watch?v=......&quot;</span>
<span class="n">current</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">get_subscription</span><span class="p">()</span>
<span class="n">my_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;my-group&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;uksouth&quot;</span><span class="p">)</span>
<span class="n">my_board</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">dashboard</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;my-board&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">my_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">my_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;source&quot;</span><span class="p">:</span> <span class="s2">&quot;managed&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">dashboard_properties</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;&quot;&quot;</span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">   &quot;lenses&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">        &quot;0&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">            &quot;order&quot;: 0,</span>
<span class="s2">            &quot;parts&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                &quot;0&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                    &quot;position&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;x&quot;: 0,</span>
<span class="s2">                        &quot;y&quot;: 0,</span>
<span class="s2">                        &quot;rowSpan&quot;: 2,</span>
<span class="s2">                        &quot;colSpan&quot;: 3</span>
<span class="s2">                    </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">                    &quot;metadata&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;inputs&quot;: [],</span>
<span class="s2">                        &quot;type&quot;: &quot;Extension/HubsExtension/PartType/MarkdownPart&quot;,</span>
<span class="s2">                        &quot;settings&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                            &quot;content&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                                &quot;settings&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                                    &quot;content&quot;: &quot;</span><span class="si">{</span><span class="n">md_content</span><span class="si">}</span><span class="s2">&quot;,</span>
<span class="s2">                                    &quot;subtitle&quot;: &quot;&quot;,</span>
<span class="s2">                                    &quot;title&quot;: &quot;&quot;</span>
<span class="s2">                                </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                            </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                        </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,               </span>
<span class="s2">                &quot;1&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                    &quot;position&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;x&quot;: 5,</span>
<span class="s2">                        &quot;y&quot;: 0,</span>
<span class="s2">                        &quot;rowSpan&quot;: 4,</span>
<span class="s2">                        &quot;colSpan&quot;: 6</span>
<span class="s2">                    </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">                    &quot;metadata&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;inputs&quot;: [],</span>
<span class="s2">                        &quot;type&quot;: &quot;Extension/HubsExtension/PartType/VideoPart&quot;,</span>
<span class="s2">                        &quot;settings&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                            &quot;content&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                                &quot;settings&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                                    &quot;title&quot;: &quot;Important Information&quot;,</span>
<span class="s2">                                    &quot;subtitle&quot;: &quot;&quot;,</span>
<span class="s2">                                    &quot;src&quot;: &quot;</span><span class="si">{</span><span class="n">video_link</span><span class="si">}</span><span class="s2">&quot;,</span>
<span class="s2">                                    &quot;autoplay&quot;: true</span>
<span class="s2">                                </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                            </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                        </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">                &quot;2&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                    &quot;position&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;x&quot;: 0,</span>
<span class="s2">                        &quot;y&quot;: 4,</span>
<span class="s2">                        &quot;rowSpan&quot;: 4,</span>
<span class="s2">                        &quot;colSpan&quot;: 6</span>
<span class="s2">                    </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">                    &quot;metadata&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;inputs&quot;: [</span>
<span class="s2">                            </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                                &quot;name&quot;: &quot;ComponentId&quot;,</span>
<span class="s2">                                &quot;value&quot;: &quot;/subscriptions/</span><span class="si">{</span><span class="n">current</span><span class="o">.</span><span class="n">subscription_id</span><span class="si">}</span><span class="s2">/resourceGroups/myRG/providers/microsoft.insights/components/myWebApp&quot;</span>
<span class="s2">                            </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                        ],</span>
<span class="s2">                        &quot;type&quot;: &quot;Extension/AppInsightsExtension/PartType/AppMapGalPt&quot;,</span>
<span class="s2">                        &quot;settings&quot;: </span><span class="se">{{}}</span><span class="s2">,</span>
<span class="s2">                        &quot;asset&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                            &quot;idInputName&quot;: &quot;ComponentId&quot;,</span>
<span class="s2">                            &quot;type&quot;: &quot;ApplicationInsights&quot;</span>
<span class="s2">                        </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                </span><span class="se">&#x7D;&#x7D;</span><span class="s2">              </span>
<span class="s2">            </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">        </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">    </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">    &quot;metadata&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">        &quot;model&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">            &quot;timeRange&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                &quot;value&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                    &quot;relative&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;duration&quot;: 24,</span>
<span class="s2">                        &quot;timeUnit&quot;: 1</span>
<span class="s2">                    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">                &quot;type&quot;: &quot;MsPortalFx.Composition.Configuration.ValueTypes.TimeRange&quot;</span>
<span class="s2">            </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">            &quot;filterLocale&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                &quot;value&quot;: &quot;en-us&quot;</span>
<span class="s2">            </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">            &quot;filters&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                &quot;value&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                    &quot;MsPortalFx_TimeRange&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;model&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                            &quot;format&quot;: &quot;utc&quot;,</span>
<span class="s2">                            &quot;granularity&quot;: &quot;auto&quot;,</span>
<span class="s2">                            &quot;relative&quot;: &quot;24h&quot;</span>
<span class="s2">                        </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">                        &quot;displayCache&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                            &quot;name&quot;: &quot;UTC Time&quot;,</span>
<span class="s2">                            &quot;value&quot;: &quot;Past 24 hours&quot;</span>
<span class="s2">                        </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">                        &quot;filteredPartIds&quot;: [</span>
<span class="s2">                            &quot;StartboardPart-UnboundPart-ae44fef5-76b8-46b0-86f0-2b3f47bad1c7&quot;</span>
<span class="s2">                        ]</span>
<span class="s2">                    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">            </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">        </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON data representing dashboard body. See above for details on how to obtain this from the Portal.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Dashboard. This should be be 64 chars max, only alphanumeric and hyphens (no spaces). For a more friendly display name, add the <code class="docutils literal notranslate"><span class="pre">hidden-title</span></code> tag.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the dashboard.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.dashboard.Dashboard.dashboard_properties">
<code class="sig-name descname">dashboard_properties</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard.dashboard_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON data representing dashboard body. See above for details on how to obtain this from the Portal.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.dashboard.Dashboard.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.dashboard.Dashboard.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Shared Dashboard. This should be be 64 chars max, only alphanumeric and hyphens (no spaces). For a more friendly display name, add the <code class="docutils literal notranslate"><span class="pre">hidden-title</span></code> tag.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.dashboard.Dashboard.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the dashboard.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.dashboard.Dashboard.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.dashboard.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON data representing dashboard body. See above for details on how to obtain this from the Portal.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Dashboard. This should be be 64 chars max, only alphanumeric and hyphens (no spaces). For a more friendly display name, add the <code class="docutils literal notranslate"><span class="pre">hidden-title</span></code> tag.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the dashboard.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.dashboard.Dashboard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.dashboard.Dashboard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.dashboard.Dashboard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
