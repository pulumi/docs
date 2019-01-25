<div class="section" id="module-pulumi_gcp.containeranalysis">
<span id="containeranalysis"></span><h1>containeranalysis<a class="headerlink" href="#module-pulumi_gcp.containeranalysis" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.containeranalysis.Note">
<em class="property">class </em><code class="descclassname">pulumi_gcp.containeranalysis.</code><code class="descname">Note</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>attestation_authority=None</em>, <em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a detailed description of a Note.</p>
<p>&gt; <strong>Warning:</strong> This resource is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta resources.</p>
<p>To get more information about Note, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/container-analysis/api/reference/rest/">https://cloud.google.com/container-analysis/api/reference/rest/</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/container-analysis/">https://cloud.google.com/container-analysis/</a>)</li>
</ul>
</dd>
</dl>
</li>
</ul>
<dl class="docutils">
<dt>&lt;div class = “oics-button” style=”float: right; margin: 0 0 -15px”&gt;</dt>
<dd><dl class="first docutils">
<dt>&lt;a href=”<a class="reference external" href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=container_analysis_note_basic&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md">https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&amp;cloudshell_working_dir=container_analysis_note_basic&amp;cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&amp;open_in_editor=main.tf&amp;cloudshell_print=.%2Fmotd&amp;cloudshell_tutorial=.%2Ftutorial.md</a>” target=”_blank”&gt;</dt>
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
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] attestation_authority
:param pulumi.Input[str] name
:param pulumi.Input[str] project</p>
<dl class="method">
<dt id="pulumi_gcp.containeranalysis.Note.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.containeranalysis.Note.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.containeranalysis.Note.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
