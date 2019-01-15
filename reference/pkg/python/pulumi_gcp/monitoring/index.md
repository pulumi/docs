<div class="section" id="module-pulumi_gcp.monitoring">
<span id="monitoring"></span><h1>monitoring<a class="headerlink" href="#module-pulumi_gcp.monitoring" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.monitoring.AlertPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.monitoring.</code><code class="descname">AlertPolicy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>combiner=None</em>, <em>conditions=None</em>, <em>display_name=None</em>, <em>enabled=None</em>, <em>labels=None</em>, <em>notification_channels=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the conditions under which some aspect of your system is
considered to be “unhealthy” and the ways to notify people or services
about this state.</p>
<p>To get more information about AlertPolicy, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/monitoring/alerts/">https://cloud.google.com/monitoring/alerts/</a>)</li>
</ul>
</dd>
</dl>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] combiner
:param pulumi.Input[list] conditions
:param pulumi.Input[str] display_name
:param pulumi.Input[bool] enabled
:param pulumi.Input[list] labels
:param pulumi.Input[list] notification_channels
:param pulumi.Input[str] project</p>
<dl class="method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.Group">
<em class="property">class </em><code class="descclassname">pulumi_gcp.monitoring.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>display_name=None</em>, <em>filter=None</em>, <em>is_cluster=None</em>, <em>parent_name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of a dynamic collection of monitored resources. Each group
has a filter that is matched against monitored resources and their
associated metadata. If a group’s filter matches an available monitored
resource, then that resource is a member of that group.</p>
<p>To get more information about Group, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/monitoring/groups/">https://cloud.google.com/monitoring/groups/</a>)</li>
</ul>
</dd>
</dl>
</li>
</ul>
<dl class="docutils">
<dt>&lt;div class = “oics-button” style=”float: right; margin: 0 0 -15px”&gt;</dt>
<dd><dl class="first docutils">
<dt>&lt;a href=”<a class="reference external" href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=monitoring_group_basic&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md">https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=monitoring_group_basic&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md</a>” target=”_blank”&gt;</dt>
<dd>&lt;img alt=”Open in Cloud Shell” src=”//gstatic.com/cloudssh/images/open-btn.svg” style=”max-height: 44px; margin: 32px auto; max-width: 100%;”&gt;</dd>
</dl>
<p class="last">&lt;/a&gt;</p>
</dd>
</dl>
<p>&lt;/div&gt;</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] display_name
:param pulumi.Input[str] filter
:param pulumi.Input[bool] is_cluster
:param pulumi.Input[str] parent_name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.NotificationChannel">
<em class="property">class </em><code class="descclassname">pulumi_gcp.monitoring.</code><code class="descname">NotificationChannel</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>enabled=None</em>, <em>labels=None</em>, <em>project=None</em>, <em>type=None</em>, <em>user_labels=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>A NotificationChannel is a medium through which an alert is delivered
when a policy violation is detected. Examples of channels include email, SMS,
and third-party messaging applications. Fields containing sensitive information
like authentication tokens or contact info are only partially populated on retrieval.</p>
<p>To get more information about NotificationChannel, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/monitoring/api/v3/">https://cloud.google.com/monitoring/api/v3/</a>)</li>
</ul>
</dd>
</dl>
</li>
</ul>
<dl class="docutils">
<dt>&lt;div class = “oics-button” style=”float: right; margin: 0 0 -15px”&gt;</dt>
<dd><dl class="first docutils">
<dt>&lt;a href=”<a class="reference external" href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=notification_channel_basic&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md">https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=notification_channel_basic&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md</a>” target=”_blank”&gt;</dt>
<dd>&lt;img alt=”Open in Cloud Shell” src=”//gstatic.com/cloudssh/images/open-btn.svg” style=”max-height: 44px; margin: 32px auto; max-width: 100%;”&gt;</dd>
</dl>
<p class="last">&lt;/a&gt;</p>
</dd>
</dl>
<p>&lt;/div&gt;</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[str] display_name
:param pulumi.Input[bool] enabled
:param pulumi.Input[dict] labels
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] type
:param pulumi.Input[dict] user_labels</p>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig">
<em class="property">class </em><code class="descclassname">pulumi_gcp.monitoring.</code><code class="descname">UptimeCheckConfig</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>content_matchers=None</em>, <em>display_name=None</em>, <em>http_check=None</em>, <em>internal_checkers=None</em>, <em>is_internal=None</em>, <em>monitored_resource=None</em>, <em>period=None</em>, <em>project=None</em>, <em>resource_group=None</em>, <em>selected_regions=None</em>, <em>tcp_check=None</em>, <em>timeout=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>This message configures which resources and services to monitor for availability.</p>
<p>To get more information about UptimeCheckConfig, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/monitoring/api/v3/">https://cloud.google.com/monitoring/api/v3/</a>)</li>
</ul>
</dd>
</dl>
</li>
</ul>
<dl class="docutils">
<dt>&lt;div class = “oics-button” style=”float: right; margin: 0 0 -15px”&gt;</dt>
<dd><dl class="first docutils">
<dt>&lt;a href=”<a class="reference external" href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=uptime_check_config_http&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md">https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=uptime_check_config_http&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md</a>” target=”_blank”&gt;</dt>
<dd>&lt;img alt=”Open in Cloud Shell” src=”//gstatic.com/cloudssh/images/open-btn.svg” style=”max-height: 44px; margin: 32px auto; max-width: 100%;”&gt;</dd>
</dl>
<p class="last">&lt;/a&gt;</p>
</dd>
</dl>
<p>&lt;/div&gt;</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] content_matchers
:param pulumi.Input[str] display_name
:param pulumi.Input[dict] http_check
:param pulumi.Input[list] internal_checkers
:param pulumi.Input[bool] is_internal
:param pulumi.Input[dict] monitored_resource
:param pulumi.Input[str] period
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[dict] resource_group
:param pulumi.Input[list] selected_regions
:param pulumi.Input[dict] tcp_check
:param pulumi.Input[str] timeout</p>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
