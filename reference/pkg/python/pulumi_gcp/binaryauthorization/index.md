<div class="section" id="module-pulumi_gcp.binaryauthorization">
<span id="binaryauthorization"></span><h1>binaryauthorization<a class="headerlink" href="#module-pulumi_gcp.binaryauthorization" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.binaryauthorization.Attestor">
<em class="property">class </em><code class="descclassname">pulumi_gcp.binaryauthorization.</code><code class="descname">Attestor</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>attestation_authority_note=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor" title="Permalink to this definition">¶</a></dt>
<dd><p>An attestor that attests to container image artifacts.</p>
<p>&gt; <strong>Warning:</strong> This resource is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta resources.</p>
<p>To get more information about Attestor, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/binary-authorization/docs/reference/rest/">https://cloud.google.com/binary-authorization/docs/reference/rest/</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/binary-authorization/">https://cloud.google.com/binary-authorization/</a>)</li>
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
<p>:param pulumi.Input[dict] attestation_authority_note
:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] project</p>
<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.Attestor.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.Attestor.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Attestor.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.binaryauthorization.Policy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.binaryauthorization.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>admission_whitelist_patterns=None</em>, <em>cluster_admission_rules=None</em>, <em>default_admission_rule=None</em>, <em>description=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy for container image binary authorization.</p>
<p>&gt; <strong>Warning:</strong> This resource is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta resources.</p>
<p>To get more information about Policy, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/binary-authorization/docs/reference/rest/">https://cloud.google.com/binary-authorization/docs/reference/rest/</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/binary-authorization/">https://cloud.google.com/binary-authorization/</a>)</li>
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
<p>:param pulumi.Input[list] admission_whitelist_patterns
:param pulumi.Input[list] cluster_admission_rules
:param pulumi.Input[dict] default_admission_rule
:param pulumi.Input[str] description
:param pulumi.Input[str] project</p>
<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.binaryauthorization.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.binaryauthorization.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
