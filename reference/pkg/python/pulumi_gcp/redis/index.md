<div class="section" id="module-pulumi_gcp.redis">
<span id="redis"></span><h1>redis<a class="headerlink" href="#module-pulumi_gcp.redis" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.redis.Instance">
<em class="property">class </em><code class="descclassname">pulumi_gcp.redis.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>alternative_location_id=None</em>, <em>authorized_network=None</em>, <em>display_name=None</em>, <em>labels=None</em>, <em>location_id=None</em>, <em>memory_size_gb=None</em>, <em>name=None</em>, <em>project=None</em>, <em>redis_configs=None</em>, <em>redis_version=None</em>, <em>region=None</em>, <em>reserved_ip_range=None</em>, <em>tier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.redis.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>A Google Cloud Redis instance.</p>
<p>To get more information about Instance, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/memorystore/docs/redis/reference/rest/">https://cloud.google.com/memorystore/docs/redis/reference/rest/</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/memorystore/docs/redis/">https://cloud.google.com/memorystore/docs/redis/</a>)</li>
</ul>
</dd>
</dl>
</li>
</ul>
<dl class="docutils">
<dt>&lt;div class = “oics-button” style=”float: right; margin: 0 0 -15px”&gt;</dt>
<dd><dl class="first docutils">
<dt>&lt;a href=”<a class="reference external" href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=redis_instance_basic&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md">https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=redis_instance_basic&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md</a>” target=”_blank”&gt;</dt>
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
<p>:param pulumi.Input[str] alternative_location_id
:param pulumi.Input[str] authorized_network
:param pulumi.Input[str] display_name
:param pulumi.Input[dict] labels
:param pulumi.Input[str] location_id
:param pulumi.Input[int] memory_size_gb
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[dict] redis_configs
:param pulumi.Input[str] redis_version
:param pulumi.Input[str] region
:param pulumi.Input[str] reserved_ip_range
:param pulumi.Input[str] tier</p>
<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.redis.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.redis.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.redis.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.redis.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
