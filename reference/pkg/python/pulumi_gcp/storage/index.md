<div class="section" id="module-pulumi_gcp.storage">
<span id="storage"></span><h1>storage<a class="headerlink" href="#module-pulumi_gcp.storage" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.storage.Bucket">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">Bucket</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cors=None</em>, <em>encryption=None</em>, <em>force_destroy=None</em>, <em>labels=None</em>, <em>lifecycle_rules=None</em>, <em>location=None</em>, <em>logging=None</em>, <em>name=None</em>, <em>project=None</em>, <em>storage_class=None</em>, <em>versioning=None</em>, <em>websites=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.Bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new bucket in Google cloud storage service (GCS).
Once a bucket has been created, its location can’t be changed.
<a class="reference external" href="https://cloud.google.com/storage/docs/access-control/lists">ACLs</a> can be applied
using the <cite>``google_storage_bucket_acl`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/google/r/storage_bucket_acl.html">https://www.terraform.io/docs/providers/google/r/storage_bucket_acl.html</a>&gt;`_.</p>
<p>For more information see
<a class="reference external" href="https://cloud.google.com/storage/docs/overview">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/buckets">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The bucket’s <a class="reference external" href="https://www.w3.org/TR/cors/">Cross-Origin Resource Sharing (CORS)</a> configuration. Multiple blocks of this type are permitted. Structure is documented below.</li>
<li><strong>encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The bucket’s encryption configuration.</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When deleting a bucket, this
boolean option will delete all contained objects. If you try to delete a
bucket that contains objects, Terraform will fail that run.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to the bucket.</li>
<li><strong>lifecycle_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The bucket’s <a class="reference external" href="https://cloud.google.com/storage/docs/lifecycle#configuration">Lifecycle Rules</a> configuration. Multiple blocks of this type are permitted. Structure is documented below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://cloud.google.com/storage/docs/bucket-locations">GCS location</a></li>
<li><strong>logging</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The bucket’s <a class="reference external" href="https://cloud.google.com/storage/docs/access-logs">Access &amp; Storage Logs</a> configuration.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://cloud.google.com/storage/docs/storage-classes">Storage Class</a> of the new bucket. Supported values include: <code class="docutils literal notranslate"><span class="pre">MULTI_REGIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">NEARLINE</span></code>, <code class="docutils literal notranslate"><span class="pre">COLDLINE</span></code>.</li>
<li><strong>versioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The bucket’s <a class="reference external" href="https://cloud.google.com/storage/docs/object-versioning">Versioning</a> configuration.</li>
<li><strong>websites</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration if the bucket acts as a website. Structure is documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.cors">
<code class="descname">cors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.cors" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s <a class="reference external" href="https://www.w3.org/TR/cors/">Cross-Origin Resource Sharing (CORS)</a> configuration. Multiple blocks of this type are permitted. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.encryption">
<code class="descname">encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s encryption configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>When deleting a bucket, this
boolean option will delete all contained objects. If you try to delete a
bucket that contains objects, Terraform will fail that run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.lifecycle_rules">
<code class="descname">lifecycle_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.lifecycle_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s <a class="reference external" href="https://cloud.google.com/storage/docs/lifecycle#configuration">Lifecycle Rules</a> configuration. Multiple blocks of this type are permitted. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://cloud.google.com/storage/docs/bucket-locations">GCS location</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.logging">
<code class="descname">logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.logging" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s <a class="reference external" href="https://cloud.google.com/storage/docs/access-logs">Access &amp; Storage Logs</a> configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.storage_class">
<code class="descname">storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://cloud.google.com/storage/docs/storage-classes">Storage Class</a> of the new bucket. Supported values include: <code class="docutils literal notranslate"><span class="pre">MULTI_REGIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">NEARLINE</span></code>, <code class="docutils literal notranslate"><span class="pre">COLDLINE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The base URL of the bucket, in the format <code class="docutils literal notranslate"><span class="pre">gs://&lt;bucket-name&gt;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.versioning">
<code class="descname">versioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.versioning" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s <a class="reference external" href="https://cloud.google.com/storage/docs/object-versioning">Versioning</a> configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Bucket.websites">
<code class="descname">websites</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Bucket.websites" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration if the bucket acts as a website. Structure is documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.Bucket.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.Bucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.Bucket.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.Bucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.BucketACL">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">BucketACL</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>default_acl=None</em>, <em>predefined_acl=None</em>, <em>role_entities=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketACL" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new bucket ACL in Google cloud storage service (GCS). For more information see 
<a class="reference external" href="https://cloud.google.com/storage/docs/access-control/lists">the official documentation</a> 
and 
<a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket it applies to.</li>
<li><strong>default_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configure this ACL to be the default ACL.</li>
<li><strong>predefined_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://cloud.google.com/storage/docs/access-control/lists#predefined-acl">canned GCS ACL</a> to apply. Must be set if <code class="docutils literal notranslate"><span class="pre">role_entity</span></code> is not.</li>
<li><strong>role_entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of role/entity pairs in the form <code class="docutils literal notranslate"><span class="pre">ROLE:entity</span></code>. See <a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls">GCS Bucket ACL documentation</a>  for more details. Must be set if <code class="docutils literal notranslate"><span class="pre">predefined_acl</span></code> is not.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketACL.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketACL.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket it applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketACL.default_acl">
<code class="descname">default_acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketACL.default_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Configure this ACL to be the default ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketACL.predefined_acl">
<code class="descname">predefined_acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketACL.predefined_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://cloud.google.com/storage/docs/access-control/lists#predefined-acl">canned GCS ACL</a> to apply. Must be set if <code class="docutils literal notranslate"><span class="pre">role_entity</span></code> is not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketACL.role_entities">
<code class="descname">role_entities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketACL.role_entities" title="Permalink to this definition">¶</a></dt>
<dd><p>List of role/entity pairs in the form <code class="docutils literal notranslate"><span class="pre">ROLE:entity</span></code>. See <a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls">GCS Bucket ACL documentation</a>  for more details. Must be set if <code class="docutils literal notranslate"><span class="pre">predefined_acl</span></code> is not.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.BucketACL.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketACL.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.BucketACL.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketACL.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.BucketIAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">BucketIAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>members=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for storage bucket. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the storage bucket are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the storage bucket are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_policy</span></code>: Setting a policy removes all other permissions on the bucket, and if done incorrectly, there’s a real chance you will lock yourself out of the bucket. If possible for your use case, using multiple google_storage_bucket_iam_binding resources will be much safer. See the usage example on how to work with policy correctly.</li>
</ul>
<blockquote>
<div><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket it applies to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] members
:param pulumi.Input[str] role: The role that should be applied. Note that custom roles must be of the format</p>
<blockquote>
<div><code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketIAMBinding.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMBinding.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket it applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketIAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the storage bucket’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketIAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.BucketIAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.BucketIAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.BucketIAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">BucketIAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>member=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for storage bucket. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the storage bucket are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the storage bucket are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_policy</span></code>: Setting a policy removes all other permissions on the bucket, and if done incorrectly, there’s a real chance you will lock yourself out of the bucket. If possible for your use case, using multiple google_storage_bucket_iam_binding resources will be much safer. See the usage example on how to work with policy correctly.</li>
</ul>
<blockquote>
<div><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket it applies to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] member
:param pulumi.Input[str] role: The role that should be applied. Note that custom roles must be of the format</p>
<blockquote>
<div><code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketIAMMember.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMMember.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket it applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketIAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the storage bucket’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketIAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.BucketIAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.BucketIAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.BucketIAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">BucketIAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>policy_data=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for storage bucket. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the storage bucket are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the storage bucket are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_policy</span></code>: Setting a policy removes all other permissions on the bucket, and if done incorrectly, there’s a real chance you will lock yourself out of the bucket. If possible for your use case, using multiple google_storage_bucket_iam_binding resources will be much safer. See the usage example on how to work with policy correctly.</li>
</ul>
<blockquote>
<div><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_storage_bucket_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket it applies to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] policy_data</p>
<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketIAMPolicy.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMPolicy.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket it applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketIAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the storage bucket’s IAM policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.BucketIAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.BucketIAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.BucketObject">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">BucketObject</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>cache_control=None</em>, <em>content=None</em>, <em>content_disposition=None</em>, <em>content_encoding=None</em>, <em>content_language=None</em>, <em>content_type=None</em>, <em>detect_md5hash=None</em>, <em>name=None</em>, <em>source=None</em>, <em>storage_class=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketObject" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new object inside an existing bucket in Google cloud storage service (GCS). 
<a class="reference external" href="https://cloud.google.com/storage/docs/access-control/lists">ACLs</a> can be applied using the <code class="docutils literal notranslate"><span class="pre">google_storage_object_acl</span></code> resource.</p>
<blockquote>
<div>For more information see</div></blockquote>
<p><a class="reference external" href="https://cloud.google.com/storage/docs/key-terms#objects">the official documentation</a> 
and 
<a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/objects">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the containing bucket.</li>
<li><strong>cache_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <a class="reference external" href="https://tools.ietf.org/html/rfc7234#section-5.2">Cache-Control</a>
directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600</li>
<li><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Data as <code class="docutils literal notranslate"><span class="pre">string</span></code> to be uploaded. Must be defined if
<code class="docutils literal notranslate"><span class="pre">source</span></code> is not.</li>
<li><strong>content_disposition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <a class="reference external" href="https://tools.ietf.org/html/rfc6266">Content-Disposition</a> of the object data.</li>
<li><strong>content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <a class="reference external" href="https://tools.ietf.org/html/rfc7231#section-3.1.2.2">Content-Encoding</a> of the object data.</li>
<li><strong>content_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <a class="reference external" href="https://tools.ietf.org/html/rfc7231#section-3.1.3.2">Content-Language</a> of the object data.</li>
<li><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <a class="reference external" href="https://tools.ietf.org/html/rfc7231#section-3.1.1.5">Content-Type</a> of the object data. Defaults to “application/octet-stream” or “text/plain; charset=utf-8”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] detect_md5hash
:param pulumi.Input[str] name: The name of the object.
:param pulumi.Input[pulumi.Archive] source: A path to the data you want to upload. Must be defined</p>
<blockquote>
<div>if <code class="docutils literal notranslate"><span class="pre">content</span></code> is not.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>storage_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://cloud.google.com/storage/docs/storage-classes">StorageClass</a> of the new bucket object.
Supported values include: <code class="docutils literal notranslate"><span class="pre">MULTI_REGIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">NEARLINE</span></code>, <code class="docutils literal notranslate"><span class="pre">COLDLINE</span></code>. If not provided, this defaults to the bucket’s default
storage class or to a <a class="reference external" href="https://cloud.google.com/storage/docs/storage-classes#standard">standard</a> class.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the containing bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.cache_control">
<code class="descname">cache_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.cache_control" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://tools.ietf.org/html/rfc7234#section-5.2">Cache-Control</a>
directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.content" title="Permalink to this definition">¶</a></dt>
<dd><p>Data as <code class="docutils literal notranslate"><span class="pre">string</span></code> to be uploaded. Must be defined if
<code class="docutils literal notranslate"><span class="pre">source</span></code> is not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.content_disposition">
<code class="descname">content_disposition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.content_disposition" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://tools.ietf.org/html/rfc6266">Content-Disposition</a> of the object data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.content_encoding">
<code class="descname">content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://tools.ietf.org/html/rfc7231#section-3.1.2.2">Content-Encoding</a> of the object data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.content_language">
<code class="descname">content_language</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.content_language" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://tools.ietf.org/html/rfc7231#section-3.1.3.2">Content-Language</a> of the object data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://tools.ietf.org/html/rfc7231#section-3.1.1.5">Content-Type</a> of the object data. Defaults to “application/octet-stream” or “text/plain; charset=utf-8”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.crc32c">
<code class="descname">crc32c</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.crc32c" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) Base 64 CRC32 hash of the uploaded data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.md5hash">
<code class="descname">md5hash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.md5hash" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) Base 64 MD5 hash of the uploaded data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.source">
<code class="descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.source" title="Permalink to this definition">¶</a></dt>
<dd><p>A path to the data you want to upload. Must be defined
if <code class="docutils literal notranslate"><span class="pre">content</span></code> is not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.BucketObject.storage_class">
<code class="descname">storage_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.storage_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://cloud.google.com/storage/docs/storage-classes">StorageClass</a> of the new bucket object.
Supported values include: <code class="docutils literal notranslate"><span class="pre">MULTI_REGIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">NEARLINE</span></code>, <code class="docutils literal notranslate"><span class="pre">COLDLINE</span></code>. If not provided, this defaults to the bucket’s default
storage class or to a <a class="reference external" href="https://cloud.google.com/storage/docs/storage-classes#standard">standard</a> class.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.BucketObject.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.BucketObject.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.BucketObject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.DefaultObjectACL">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">DefaultObjectACL</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>role_entities=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.DefaultObjectACL" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new default object ACL in Google Cloud Storage service (GCS). For more information see</p>
<blockquote>
<div>Note that for each object, its creator will have the <code class="docutils literal notranslate"><span class="pre">&quot;OWNER&quot;</span></code> role in addition
to the default ACL that has been defined.</div></blockquote>
<p>For more information see
<a class="reference external" href="https://cloud.google.com/storage/docs/access-control/lists">the official documentation</a> 
and 
<a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls">API</a>.</p>
<blockquote>
<div>Want fine-grained control over default object ACLs? Use <code class="docutils literal notranslate"><span class="pre">google_storage_default_object_access_control</span></code>
to control individual role entity pairs.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket it applies to.</li>
<li><strong>role_entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of role/entity pairs in the form <code class="docutils literal notranslate"><span class="pre">ROLE:entity</span></code>. See <a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls">GCS Object ACL documentation</a> for more details.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.storage.DefaultObjectACL.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.DefaultObjectACL.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket it applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.DefaultObjectACL.role_entities">
<code class="descname">role_entities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.DefaultObjectACL.role_entities" title="Permalink to this definition">¶</a></dt>
<dd><p>List of role/entity pairs in the form <code class="docutils literal notranslate"><span class="pre">ROLE:entity</span></code>. See <a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls">GCS Object ACL documentation</a> for more details.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.DefaultObjectACL.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.DefaultObjectACL.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.DefaultObjectACL.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.DefaultObjectACL.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.DefaultObjectAccessControl">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">DefaultObjectAccessControl</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>entity=None</em>, <em>object=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.DefaultObjectAccessControl" title="Permalink to this definition">¶</a></dt>
<dd><p>The DefaultObjectAccessControls resources represent the Access Control
Lists (ACLs) applied to a new object within a Google Cloud Storage bucket
when no ACL was provided for that object. ACLs let you specify who has
access to your bucket contents and to what extent.</p>
<p>There are two roles that can be assigned to an entity:</p>
<p>READERs can get an object, though the acl property will not be revealed.
OWNERs are READERs, and they can get the acl property, update an object,
and call all objectAccessControls methods on the object. The owner of an
object is always an OWNER.
For more information, see Access Control, with the caveat that this API
uses READER and OWNER instead of READ and FULL_CONTROL.</p>
<p>To get more information about DefaultObjectAccessControl, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/storage/docs/access-control/create-manage-lists">Official Documentation</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=storage_default_object_access_control_public&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] bucket
:param pulumi.Input[str] entity
:param pulumi.Input[str] object
:param pulumi.Input[str] role</p>
<dl class="method">
<dt id="pulumi_gcp.storage.DefaultObjectAccessControl.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.DefaultObjectAccessControl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.DefaultObjectAccessControl.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.DefaultObjectAccessControl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.GetObjectSignedUrlResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">GetObjectSignedUrlResult</code><span class="sig-paren">(</span><em>signed_url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.GetObjectSignedUrlResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getObjectSignedUrl.</p>
<dl class="attribute">
<dt id="pulumi_gcp.storage.GetObjectSignedUrlResult.signed_url">
<code class="descname">signed_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.GetObjectSignedUrlResult.signed_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The signed URL that can be used to access the storage object without authentication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.GetObjectSignedUrlResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.GetObjectSignedUrlResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.storage.GetProjectServiceAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">GetProjectServiceAccountResult</code><span class="sig-paren">(</span><em>email_address=None</em>, <em>project=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.GetProjectServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjectServiceAccount.</p>
<dl class="attribute">
<dt id="pulumi_gcp.storage.GetProjectServiceAccountResult.email_address">
<code class="descname">email_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.GetProjectServiceAccountResult.email_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the service account. This value is often used to refer to the service account
in order to grant IAM permissions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.GetProjectServiceAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.GetProjectServiceAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.storage.Notification">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">Notification</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>custom_attributes=None</em>, <em>event_types=None</em>, <em>object_name_prefix=None</em>, <em>payload_format=None</em>, <em>topic=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.Notification" title="Permalink to this definition">¶</a></dt>
<dd><dl class="docutils">
<dt>Creates a new notification configuration on a specified bucket, establishing a flow of event notifications from GCS to a Cloud Pub/Sub topic.</dt>
<dd>For more information see</dd>
</dl>
<p><a class="reference external" href="https://cloud.google.com/storage/docs/pubsub-notifications">the official documentation</a> 
and 
<a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/notifications">API</a>.</p>
<p>In order to enable notifications, a special Google Cloud Storage service account unique to the project
must have the IAM permission “projects.topics.publish” for a Cloud Pub/Sub topic in the project. To get the service
account’s email address, use the <code class="docutils literal notranslate"><span class="pre">google_storage_project_service_account</span></code> datasource’s <code class="docutils literal notranslate"><span class="pre">email_address</span></code> value, and see below
for an example of enabling notifications by granting the correct IAM permission. See
<a class="reference external" href="https://cloud.google.com/storage/docs/gsutil/commands/notification">the notifications documentation</a> for more details.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket.</li>
<li><strong>custom_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription</li>
<li><strong>event_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: <code class="docutils literal notranslate"><span class="pre">&quot;OBJECT_FINALIZE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OBJECT_METADATA_UPDATE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OBJECT_DELETE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OBJECT_ARCHIVE&quot;</span></code></li>
<li><strong>object_name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.</li>
<li><strong>payload_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired content of the Payload. One of <code class="docutils literal notranslate"><span class="pre">&quot;JSON_API_V1&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</li>
<li><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. <code class="docutils literal notranslate"><span class="pre">projects/my-gcp-project/topics/my-topic</span></code> or <code class="docutils literal notranslate"><span class="pre">my-topic</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.storage.Notification.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Notification.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Notification.custom_attributes">
<code class="descname">custom_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Notification.custom_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Notification.event_types">
<code class="descname">event_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Notification.event_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: <code class="docutils literal notranslate"><span class="pre">&quot;OBJECT_FINALIZE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OBJECT_METADATA_UPDATE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OBJECT_DELETE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;OBJECT_ARCHIVE&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Notification.object_name_prefix">
<code class="descname">object_name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Notification.object_name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Notification.payload_format">
<code class="descname">payload_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Notification.payload_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired content of the Payload. One of <code class="docutils literal notranslate"><span class="pre">&quot;JSON_API_V1&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Notification.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Notification.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.Notification.topic">
<code class="descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.Notification.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. <code class="docutils literal notranslate"><span class="pre">projects/my-gcp-project/topics/my-topic</span></code> or <code class="docutils literal notranslate"><span class="pre">my-topic</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.Notification.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.Notification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.Notification.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.Notification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.ObjectACL">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">ObjectACL</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>object=None</em>, <em>predefined_acl=None</em>, <em>role_entities=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.ObjectACL" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new object ACL in Google cloud storage service (GCS). For more information see 
<a class="reference external" href="https://cloud.google.com/storage/docs/access-control/lists">the official documentation</a> 
and 
<a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket it applies to.</li>
<li><strong>object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the object it applies to.</li>
<li><strong>predefined_acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://cloud.google.com/storage/docs/access-control#predefined-acl">canned GCS ACL</a> to apply. Must be set if <code class="docutils literal notranslate"><span class="pre">role_entity</span></code> is not.</p>
</li>
<li><strong>role_entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of role/entity pairs in the form <code class="docutils literal notranslate"><span class="pre">ROLE:entity</span></code>. See <a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls">GCS Object ACL documentation</a> for more details. Must be set if <code class="docutils literal notranslate"><span class="pre">predefined_acl</span></code> is not.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.storage.ObjectACL.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.ObjectACL.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket it applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.ObjectACL.object">
<code class="descname">object</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.ObjectACL.object" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the object it applies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.ObjectACL.predefined_acl">
<code class="descname">predefined_acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.ObjectACL.predefined_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://cloud.google.com/storage/docs/access-control#predefined-acl">canned GCS ACL</a> to apply. Must be set if <code class="docutils literal notranslate"><span class="pre">role_entity</span></code> is not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.storage.ObjectACL.role_entities">
<code class="descname">role_entities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.storage.ObjectACL.role_entities" title="Permalink to this definition">¶</a></dt>
<dd><p>List of role/entity pairs in the form <code class="docutils literal notranslate"><span class="pre">ROLE:entity</span></code>. See <a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls">GCS Object ACL documentation</a> for more details. Must be set if <code class="docutils literal notranslate"><span class="pre">predefined_acl</span></code> is not.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.storage.ObjectACL.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.ObjectACL.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.ObjectACL.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.ObjectACL.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.storage.ObjectAccessControl">
<em class="property">class </em><code class="descclassname">pulumi_gcp.storage.</code><code class="descname">ObjectAccessControl</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>entity=None</em>, <em>object=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.ObjectAccessControl" title="Permalink to this definition">¶</a></dt>
<dd><p>The ObjectAccessControls resources represent the Access Control Lists
(ACLs) for objects within Google Cloud Storage. ACLs let you specify
who has access to your data and to what extent.</p>
<p>There are two roles that can be assigned to an entity:</p>
<p>READERs can get an object, though the acl property will not be revealed.
OWNERs are READERs, and they can get the acl property, update an object,
and call all objectAccessControls methods on the object. The owner of an
object is always an OWNER.
For more information, see Access Control, with the caveat that this API
uses READER and OWNER instead of READ and FULL_CONTROL.</p>
<p>To get more information about ObjectAccessControl, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/storage/docs/access-control/create-manage-lists">Official Documentation</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=storage_object_access_control_public_object&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] bucket
:param pulumi.Input[str] entity
:param pulumi.Input[str] object
:param pulumi.Input[str] role</p>
<dl class="method">
<dt id="pulumi_gcp.storage.ObjectAccessControl.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.ObjectAccessControl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.storage.ObjectAccessControl.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.ObjectAccessControl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_gcp.storage.get_object_signed_url">
<code class="descclassname">pulumi_gcp.storage.</code><code class="descname">get_object_signed_url</code><span class="sig-paren">(</span><em>bucket=None</em>, <em>content_md5=None</em>, <em>content_type=None</em>, <em>credentials=None</em>, <em>duration=None</em>, <em>extension_headers=None</em>, <em>http_method=None</em>, <em>path=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.get_object_signed_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Cloud storage signed URL data source generates a signed URL for a given storage object. Signed URLs provide a way to give time-limited read or write access to anyone in possession of the URL, regardless of whether they have a Google account.</p>
<p>For more info about signed URL’s is available <a class="reference external" href="https://cloud.google.com/storage/docs/access-control/signed-urls">here</a>.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.storage.get_project_service_account">
<code class="descclassname">pulumi_gcp.storage.</code><code class="descname">get_project_service_account</code><span class="sig-paren">(</span><em>project=None</em>, <em>user_project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.storage.get_project_service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the email address of a project’s unique Google Cloud Storage service account.</p>
<p>Each Google Cloud project has a unique service account for use with Google Cloud Storage. Only this
special service account can be used to set up <code class="docutils literal notranslate"><span class="pre">google_storage_notification</span></code> resources.</p>
<p>For more information see
<a class="reference external" href="https://cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount">the API reference</a>.</p>
</dd></dl>

</div>
