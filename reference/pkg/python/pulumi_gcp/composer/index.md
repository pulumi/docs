<div class="section" id="module-pulumi_gcp.composer">
<span id="composer"></span><h1>composer<a class="headerlink" href="#module-pulumi_gcp.composer" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.composer.Environment">
<em class="property">class </em><code class="descclassname">pulumi_gcp.composer.</code><code class="descname">Environment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>config=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment" title="Permalink to this definition">¶</a></dt>
<dd><p>An environment for running orchestration tasks.</p>
<p>Environments run Apache Airflow software on Google infrastructure.</p>
<p>To get more information about Environments, see:</p>
<ul class="simple">
<li>[API documentation](<a class="reference external" href="https://cloud.google.com/composer/docs/reference/rest/">https://cloud.google.com/composer/docs/reference/rest/</a>)</li>
<li><dl class="first docutils">
<dt>How-to Guides</dt>
<dd><ul class="first last">
<li>[Official Documentation](<a class="reference external" href="https://cloud.google.com/composer/docs">https://cloud.google.com/composer/docs</a>)</li>
<li>[Configuring Shared VPC for Composer Environments](<a class="reference external" href="https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc">https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc</a>)</li>
</ul>
</dd>
</dl>
</li>
<li>[Apache Airflow Documentation](<a class="reference external" href="http://airflow.apache.org/">http://airflow.apache.org/</a>)</li>
</ul>
<dl class="docutils">
<dt>&gt; <strong>Warning:</strong> We <strong>STRONGLY</strong> recommend  you read the [GCP guides](<a class="reference external" href="https://cloud.google.com/composer/docs/how-to">https://cloud.google.com/composer/docs/how-to</a>)</dt>
<dd><p class="first">as the Environment resource requires a long deployment process and involves several layers of GCP infrastructure, 
including a Kubernetes Engine cluster, Cloud Storage, and Compute networking resources. Due to limitations of the API,
Terraform will not be able to automatically find or manage many of these underlying resources. In particular:
* It can take up to one hour to create or update an environment resource. In addition, GCP may only detect some</p>
<blockquote>
<div>errors in configuration when they are used (e.g. ~40-50 minutes into the creation process), and is prone to limited
error reporting. If you encounter confusing or uninformative errors, please verify your configuration is valid 
against GCP Cloud Composer before filing bugs against the Terraform provider.</div></blockquote>
<ul class="last simple">
<li><strong>Environments create Google Cloud Storage buckets that do not get cleaned up automatically</strong> on environment 
deletion. [More about Composer’s use of Cloud Storage](<a class="reference external" href="https://cloud.google.com/composer/docs/concepts/cloud-storage">https://cloud.google.com/composer/docs/concepts/cloud-storage</a>).</li>
</ul>
</dd>
</dl>
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
<p>:param pulumi.Input[dict] config
:param pulumi.Input[dict] labels
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region</p>
<dl class="attribute">
<dt id="pulumi_gcp.composer.Environment.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.Environment.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.composer.Environment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.composer.Environment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
