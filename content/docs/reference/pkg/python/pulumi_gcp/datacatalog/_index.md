---
title: Module datacatalog
title_tag: Module datacatalog | Package pulumi_gcp | Python SDK
linktitle: datacatalog
notitle: true
---

{{< resource-docs-alert "gcp" >}}

<div class="section" id="datacatalog">
<h1>datacatalog<a class="headerlink" href="#datacatalog" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.datacatalog"></span><dl class="py class">
<dt id="pulumi_gcp.datacatalog.Entry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.datacatalog.</code><code class="sig-name descname">Entry</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs_fileset_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linked_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_specified_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_specified_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry" title="Permalink to this definition">¶</a></dt>
<dd><p>Entry Metadata. A Data Catalog Entry resource represents another resource in Google Cloud Platform
(such as a BigQuery dataset or a Pub/Sub topic) or outside of Google Cloud Platform. Clients can use
the linkedResource field in the Entry resource to refer to the original resource ID of the source system.</p>
<p>An Entry resource contains resource details, such as its schema. An Entry can also be used to attach
flexible metadata, such as a Tag.</p>
<p>To get more information about Entry, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/data-catalog/docs">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">entry_group</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroup</span><span class="p">(</span><span class="s2">&quot;entryGroup&quot;</span><span class="p">,</span> <span class="n">entry_group_id</span><span class="o">=</span><span class="s2">&quot;my_group&quot;</span><span class="p">)</span>
<span class="n">basic_entry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">Entry</span><span class="p">(</span><span class="s2">&quot;basicEntry&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">entry_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">entry_id</span><span class="o">=</span><span class="s2">&quot;my_entry&quot;</span><span class="p">,</span>
    <span class="n">user_specified_type</span><span class="o">=</span><span class="s2">&quot;my_custom_type&quot;</span><span class="p">,</span>
    <span class="n">user_specified_system</span><span class="o">=</span><span class="s2">&quot;SomethingExternal&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">entry_group</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroup</span><span class="p">(</span><span class="s2">&quot;entryGroup&quot;</span><span class="p">,</span> <span class="n">entry_group_id</span><span class="o">=</span><span class="s2">&quot;my_group&quot;</span><span class="p">)</span>
<span class="n">basic_entry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">Entry</span><span class="p">(</span><span class="s2">&quot;basicEntry&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">entry_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">entry_id</span><span class="o">=</span><span class="s2">&quot;my_entry&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;FILESET&quot;</span><span class="p">,</span>
    <span class="n">gcs_fileset_spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;filePatterns&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;gs://fake_bucket/dir/*&quot;</span><span class="p">],</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">entry_group</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroup</span><span class="p">(</span><span class="s2">&quot;entryGroup&quot;</span><span class="p">,</span> <span class="n">entry_group_id</span><span class="o">=</span><span class="s2">&quot;my_group&quot;</span><span class="p">)</span>
<span class="n">basic_entry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">Entry</span><span class="p">(</span><span class="s2">&quot;basicEntry&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">entry_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">entry_id</span><span class="o">=</span><span class="s2">&quot;my_entry&quot;</span><span class="p">,</span>
    <span class="n">user_specified_type</span><span class="o">=</span><span class="s2">&quot;my_user_specified_type&quot;</span><span class="p">,</span>
    <span class="n">user_specified_system</span><span class="o">=</span><span class="s2">&quot;Something_custom&quot;</span><span class="p">,</span>
    <span class="n">linked_resource</span><span class="o">=</span><span class="s2">&quot;my/linked/resource&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;my custom type entry&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;a custom type entry for a user specified system&quot;</span><span class="p">,</span>
    <span class="n">schema</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;columns&quot;: [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;column&quot;: &quot;first_name&quot;,</span>
<span class="s2">      &quot;description&quot;: &quot;First name&quot;,</span>
<span class="s2">      &quot;mode&quot;: &quot;REQUIRED&quot;,</span>
<span class="s2">      &quot;type&quot;: &quot;STRING&quot;</span>
<span class="s2">    },</span>
<span class="s2">    {</span>
<span class="s2">      &quot;column&quot;: &quot;last_name&quot;,</span>
<span class="s2">      &quot;description&quot;: &quot;Last name&quot;,</span>
<span class="s2">      &quot;mode&quot;: &quot;REQUIRED&quot;,</span>
<span class="s2">      &quot;type&quot;: &quot;STRING&quot;</span>
<span class="s2">    },</span>
<span class="s2">    {</span>
<span class="s2">      &quot;column&quot;: &quot;address&quot;,</span>
<span class="s2">      &quot;description&quot;: &quot;Address&quot;,</span>
<span class="s2">      &quot;mode&quot;: &quot;REPEATED&quot;,</span>
<span class="s2">      &quot;subcolumns&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">          &quot;column&quot;: &quot;city&quot;,</span>
<span class="s2">          &quot;description&quot;: &quot;City&quot;,</span>
<span class="s2">          &quot;mode&quot;: &quot;NULLABLE&quot;,</span>
<span class="s2">          &quot;type&quot;: &quot;STRING&quot;</span>
<span class="s2">        },</span>
<span class="s2">        {</span>
<span class="s2">          &quot;column&quot;: &quot;state&quot;,</span>
<span class="s2">          &quot;description&quot;: &quot;State&quot;,</span>
<span class="s2">          &quot;mode&quot;: &quot;NULLABLE&quot;,</span>
<span class="s2">          &quot;type&quot;: &quot;STRING&quot;</span>
<span class="s2">        }</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;type&quot;: &quot;RECORD&quot;</span>
<span class="s2">    }</span>
<span class="s2">  ]</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entry description, which can consist of several sentences or paragraphs that describe entry contents.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display information such as title and description. A short name to identify the entry,
for example, “Analytics Data - Jan 2011”.</p></li>
<li><p><strong>entry_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the entry group this entry is in.</p></li>
<li><p><strong>entry_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the entry to create.</p></li>
<li><p><strong>gcs_fileset_spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.  Structure is documented below.</p></li>
<li><p><strong>linked_resource</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource this metadata entry refers to.
For Google Cloud Platform resources, linkedResource is the full name of the resource.
For example, the linkedResource for a table resource from BigQuery is:
//bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId
Output only when Entry is of type in the EntryType enum. For entries with userSpecifiedType,
this field is optional and defaults to an empty string.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Schema of the entry (e.g. BigQuery, GoogleSQL, Avro schema), as a json string. An entry might not have any schema
attached to it. See
<a class="reference external" href="https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#schema">https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#schema</a>
for what fields this schema can contain.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the entry. Only used for Entries with types in the EntryType enum.
Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use userSpecifiedType.</p></li>
<li><p><strong>user_specified_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field indicates the entry’s source system that Data Catalog does not integrate with.
userSpecifiedSystem strings must begin with a letter or underscore and can only contain letters, numbers,
and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.</p></li>
<li><p><strong>user_specified_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entry type if it does not fit any of the input-allowed values listed in EntryType enum above.
When creating an entry, users should check the enum values first, if nothing matches the entry
to be created, then provide a custom value, for example “my_special_type”.
userSpecifiedType strings must begin with a letter or underscore and can only contain letters,
numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>gcs_fileset_spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Patterns to identify a set of files in Google Cloud Storage.
See <a class="reference external" href="https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames">Cloud Storage documentation</a>
for more information. Note that bucket wildcards are currently not supported. Examples of valid filePatterns:</p>
<ul>
<li><p>gs://bucket_name/dir/<a href="#id1"><span class="problematic" id="id2">*</span></a>: matches all files within bucket_name/dir directory.</p></li>
<li><p>gs://bucket_name/dir/<a href="#id3"><span class="problematic" id="id4">**</span></a>: matches all files in bucket_name/dir spanning all subdirectories.</p></li>
<li><p>gs://bucket_name/file*: matches files prefixed by file in bucket_name</p></li>
<li><p>gs://bucket_name/??.txt: matches files with two characters followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/[aeiou].txt: matches files that contain a single vowel character followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/[a-m].txt: matches files that contain a, b, … or m followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/a/<em>/b: matches all files in bucket_name that match a/</em>/b pattern, such as a/c/b, a/d/b</p></li>
<li><p>gs://another_bucket/a.txt: matches gs://another_bucket/a.txt</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleGcsFileSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - -
Sample files contained in this fileset, not all files contained in this fileset are represented here.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The full file path</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
The size of the file, in bytes.</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.bigquery_date_sharded_spec">
<code class="sig-name descname">bigquery_date_sharded_spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.bigquery_date_sharded_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Specification for a group of BigQuery tables with name pattern [prefix]YYYYMMDD. Context:
<a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding">https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shardCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tablePrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.bigquery_table_spec">
<code class="sig-name descname">bigquery_table_spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.bigquery_table_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Specification that applies to a BigQuery table. This is only valid on entries of type TABLE.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tableSourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tableSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">groupedEntry</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">viewQuery</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Entry description, which can consist of several sentences or paragraphs that describe entry contents.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display information such as title and description. A short name to identify the entry,
for example, “Analytics Data - Jan 2011”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.entry_group">
<code class="sig-name descname">entry_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.entry_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the entry group this entry is in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.entry_id">
<code class="sig-name descname">entry_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.entry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the entry to create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.gcs_fileset_spec">
<code class="sig-name descname">gcs_fileset_spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.gcs_fileset_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Patterns to identify a set of files in Google Cloud Storage.
See <a class="reference external" href="https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames">Cloud Storage documentation</a>
for more information. Note that bucket wildcards are currently not supported. Examples of valid filePatterns:</p>
<ul>
<li><p>gs://bucket_name/dir/<a href="#id6"><span class="problematic" id="id7">*</span></a>: matches all files within bucket_name/dir directory.</p></li>
<li><p>gs://bucket_name/dir/<a href="#id8"><span class="problematic" id="id9">**</span></a>: matches all files in bucket_name/dir spanning all subdirectories.</p></li>
<li><p>gs://bucket_name/file*: matches files prefixed by file in bucket_name</p></li>
<li><p>gs://bucket_name/??.txt: matches files with two characters followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/[aeiou].txt: matches files that contain a single vowel character followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/[a-m].txt: matches files that contain a, b, … or m followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/a/<em>/b: matches all files in bucket_name that match a/</em>/b pattern, such as a/c/b, a/d/b</p></li>
<li><p>gs://another_bucket/a.txt: matches gs://another_bucket/a.txt</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleGcsFileSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - -
Sample files contained in this fileset, not all files contained in this fileset are represented here.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The full file path</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - -
The size of the file, in bytes.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.integrated_system">
<code class="sig-name descname">integrated_system</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.integrated_system" title="Permalink to this definition">¶</a></dt>
<dd><p>This field indicates the entry’s source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.linked_resource">
<code class="sig-name descname">linked_resource</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.linked_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource this metadata entry refers to.
For Google Cloud Platform resources, linkedResource is the full name of the resource.
For example, the linkedResource for a table resource from BigQuery is:
//bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId
Output only when Entry is of type in the EntryType enum. For entries with userSpecifiedType,
this field is optional and defaults to an empty string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Catalog resource name of the entry in URL format. Example:
projects/{project_id}/locations/{location}/entryGroups/{entryGroupId}/entries/{entryId}. Note that this Entry and its
child resources may not actually be stored in the location in this name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.schema">
<code class="sig-name descname">schema</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Schema of the entry (e.g. BigQuery, GoogleSQL, Avro schema), as a json string. An entry might not have any schema
attached to it. See
<a class="reference external" href="https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#schema">https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#schema</a>
for what fields this schema can contain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the entry. Only used for Entries with types in the EntryType enum.
Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use userSpecifiedType.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.user_specified_system">
<code class="sig-name descname">user_specified_system</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.user_specified_system" title="Permalink to this definition">¶</a></dt>
<dd><p>This field indicates the entry’s source system that Data Catalog does not integrate with.
userSpecifiedSystem strings must begin with a letter or underscore and can only contain letters, numbers,
and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.Entry.user_specified_type">
<code class="sig-name descname">user_specified_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.user_specified_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Entry type if it does not fit any of the input-allowed values listed in EntryType enum above.
When creating an entry, users should check the enum values first, if nothing matches the entry
to be created, then provide a custom value, for example “my_special_type”.
userSpecifiedType strings must begin with a letter or underscore and can only contain letters,
numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.Entry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_date_sharded_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_table_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs_fileset_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integrated_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linked_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_specified_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_specified_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Entry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_date_sharded_spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specification for a group of BigQuery tables with name pattern [prefix]YYYYMMDD. Context:
<a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding">https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding</a>.</p></li>
<li><p><strong>bigquery_table_spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specification that applies to a BigQuery table. This is only valid on entries of type TABLE.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entry description, which can consist of several sentences or paragraphs that describe entry contents.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display information such as title and description. A short name to identify the entry,
for example, “Analytics Data - Jan 2011”.</p></li>
<li><p><strong>entry_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the entry group this entry is in.</p></li>
<li><p><strong>entry_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the entry to create.</p></li>
<li><p><strong>gcs_fileset_spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.  Structure is documented below.</p></li>
<li><p><strong>integrated_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field indicates the entry’s source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.</p></li>
<li><p><strong>linked_resource</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource this metadata entry refers to.
For Google Cloud Platform resources, linkedResource is the full name of the resource.
For example, the linkedResource for a table resource from BigQuery is:
//bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId
Output only when Entry is of type in the EntryType enum. For entries with userSpecifiedType,
this field is optional and defaults to an empty string.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Data Catalog resource name of the entry in URL format. Example:
projects/{project_id}/locations/{location}/entryGroups/{entryGroupId}/entries/{entryId}. Note that this Entry and its
child resources may not actually be stored in the location in this name.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Schema of the entry (e.g. BigQuery, GoogleSQL, Avro schema), as a json string. An entry might not have any schema
attached to it. See
<a class="reference external" href="https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#schema">https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#schema</a>
for what fields this schema can contain.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the entry. Only used for Entries with types in the EntryType enum.
Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use userSpecifiedType.</p></li>
<li><p><strong>user_specified_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field indicates the entry’s source system that Data Catalog does not integrate with.
userSpecifiedSystem strings must begin with a letter or underscore and can only contain letters, numbers,
and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.</p></li>
<li><p><strong>user_specified_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entry type if it does not fit any of the input-allowed values listed in EntryType enum above.
When creating an entry, users should check the enum values first, if nothing matches the entry
to be created, then provide a custom value, for example “my_special_type”.
userSpecifiedType strings must begin with a letter or underscore and can only contain letters,
numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_date_sharded_spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shardCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tablePrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>bigquery_table_spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tableSourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tableSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">groupedEntry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">viewQuery</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>gcs_fileset_spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Patterns to identify a set of files in Google Cloud Storage.
See <a class="reference external" href="https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames">Cloud Storage documentation</a>
for more information. Note that bucket wildcards are currently not supported. Examples of valid filePatterns:</p>
<ul>
<li><p>gs://bucket_name/dir/<a href="#id11"><span class="problematic" id="id12">*</span></a>: matches all files within bucket_name/dir directory.</p></li>
<li><p>gs://bucket_name/dir/<a href="#id13"><span class="problematic" id="id14">**</span></a>: matches all files in bucket_name/dir spanning all subdirectories.</p></li>
<li><p>gs://bucket_name/file*: matches files prefixed by file in bucket_name</p></li>
<li><p>gs://bucket_name/??.txt: matches files with two characters followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/[aeiou].txt: matches files that contain a single vowel character followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/[a-m].txt: matches files that contain a, b, … or m followed by .txt in bucket_name</p></li>
<li><p>gs://bucket_name/a/<em>/b: matches all files in bucket_name that match a/</em>/b pattern, such as a/c/b, a/d/b</p></li>
<li><p>gs://another_bucket/a.txt: matches gs://another_bucket/a.txt</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleGcsFileSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - -
Sample files contained in this fileset, not all files contained in this fileset are represented here.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The full file path</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
The size of the file, in bytes.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.Entry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.Entry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.Entry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.EntryGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.datacatalog.</code><code class="sig-name descname">EntryGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EntryGroup resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: Entry group description, which can consist of several sentences or paragraphs that describe entry group contents.
:param pulumi.Input[str] display_name: A short name to identify the entry group, for example, “analytics data - jan 2011”.
:param pulumi.Input[str] entry_group_id: The id of the entry group to create. The id must begin with a letter or underscore,</p>
<blockquote>
<div><p>contain only English letters, numbers and underscores, and be at most 64 characters.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EntryGroup location region.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Entry group description, which can consist of several sentences or paragraphs that describe entry group contents.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroup.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name to identify the entry group, for example, “analytics data - jan 2011”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroup.entry_group_id">
<code class="sig-name descname">entry_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.entry_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the entry group to create. The id must begin with a letter or underscore,
contain only English letters, numbers and underscores, and be at most 64 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the entry group in URL format. Example:
projects/{project}/locations/{location}/entryGroups/{entryGroupId}</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroup.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroup.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>EntryGroup location region.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.EntryGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntryGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entry group description, which can consist of several sentences or paragraphs that describe entry group contents.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name to identify the entry group, for example, “analytics data - jan 2011”.</p></li>
<li><p><strong>entry_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the entry group to create. The id must begin with a letter or underscore,
contain only English letters, numbers and underscores, and be at most 64 characters.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the entry group in URL format. Example:
projects/{project}/locations/{location}/entryGroups/{entryGroupId}</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EntryGroup location region.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.EntryGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.EntryGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.EntryGroupIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.datacatalog.</code><code class="sig-name descname">EntryGroupIamBinding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Data catalog EntryGroup. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamPolicy</span></code>: Authoritative. Sets the IAM policy for the entrygroup and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the entrygroup are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the entrygroup are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_iam_policy</span><span class="p">(</span><span class="n">binding</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="s2">&quot;members&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">],</span>
<span class="p">}])</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamPolicy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">policy_data</span><span class="o">=</span><span class="n">admin</span><span class="o">.</span><span class="n">policy_data</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">binding</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamBinding</span><span class="p">(</span><span class="s2">&quot;binding&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">member</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamMember</span><span class="p">(</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">member</span><span class="o">=</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entry_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamBinding.entry_group">
<code class="sig-name descname">entry_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamBinding.entry_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamBinding.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamBinding.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntryGroupIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entry_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.EntryGroupIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.EntryGroupIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.datacatalog.</code><code class="sig-name descname">EntryGroupIamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Data catalog EntryGroup. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamPolicy</span></code>: Authoritative. Sets the IAM policy for the entrygroup and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the entrygroup are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the entrygroup are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_iam_policy</span><span class="p">(</span><span class="n">binding</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="s2">&quot;members&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">],</span>
<span class="p">}])</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamPolicy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">policy_data</span><span class="o">=</span><span class="n">admin</span><span class="o">.</span><span class="n">policy_data</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">binding</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamBinding</span><span class="p">(</span><span class="s2">&quot;binding&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">member</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamMember</span><span class="p">(</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">member</span><span class="o">=</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entry_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamMember.entry_group">
<code class="sig-name descname">entry_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamMember.entry_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamMember.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamMember.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamMember.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntryGroupIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entry_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.EntryGroupIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.EntryGroupIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.datacatalog.</code><code class="sig-name descname">EntryGroupIamPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Data catalog EntryGroup. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamPolicy</span></code>: Authoritative. Sets the IAM policy for the entrygroup and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the entrygroup are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the entrygroup are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">datacatalog.EntryGroupIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">admin</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_iam_policy</span><span class="p">(</span><span class="n">binding</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="s2">&quot;members&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">],</span>
<span class="p">}])</span>
<span class="n">policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamPolicy</span><span class="p">(</span><span class="s2">&quot;policy&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">policy_data</span><span class="o">=</span><span class="n">admin</span><span class="o">.</span><span class="n">policy_data</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">binding</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamBinding</span><span class="p">(</span><span class="s2">&quot;binding&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">member</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">EntryGroupIamMember</span><span class="p">(</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">entry_group</span><span class="o">=</span><span class="n">google_data_catalog_entry_group</span><span class="p">[</span><span class="s2">&quot;basic_entry_group&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/viewer&quot;</span><span class="p">,</span>
    <span class="n">member</span><span class="o">=</span><span class="s2">&quot;user:jane@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entry_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamPolicy.entry_group">
<code class="sig-name descname">entry_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamPolicy.entry_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamPolicy.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntryGroupIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entry_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.EntryGroupIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.EntryGroupIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.EntryGroupIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.TagTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.datacatalog.</code><code class="sig-name descname">TagTemplate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>A tag template defines a tag, which can have one or more typed fields.
The template is used to create and attach the tag to GCP resources.</p>
<p>To get more information about TagTemplate, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/data-catalog/docs">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">basic_tag_template</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">datacatalog</span><span class="o">.</span><span class="n">TagTemplate</span><span class="p">(</span><span class="s2">&quot;basicTagTemplate&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Demo Tag Template&quot;</span><span class="p">,</span>
    <span class="n">fields</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;display_name&quot;</span><span class="p">:</span> <span class="s2">&quot;Source of data asset&quot;</span><span class="p">,</span>
            <span class="s2">&quot;fieldId&quot;</span><span class="p">:</span> <span class="s2">&quot;source&quot;</span><span class="p">,</span>
            <span class="s2">&quot;isRequired&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;primitiveType&quot;</span><span class="p">:</span> <span class="s2">&quot;STRING&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;display_name&quot;</span><span class="p">:</span> <span class="s2">&quot;Number of rows in the data asset&quot;</span><span class="p">,</span>
            <span class="s2">&quot;fieldId&quot;</span><span class="p">:</span> <span class="s2">&quot;num_rows&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;primitiveType&quot;</span><span class="p">:</span> <span class="s2">&quot;DOUBLE&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;display_name&quot;</span><span class="p">:</span> <span class="s2">&quot;PII type&quot;</span><span class="p">,</span>
            <span class="s2">&quot;fieldId&quot;</span><span class="p">:</span> <span class="s2">&quot;pii_type&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;enumType&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;allowedValues&quot;</span><span class="p">:</span> <span class="p">[</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;display_name&quot;</span><span class="p">:</span> <span class="s2">&quot;EMAIL&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;display_name&quot;</span><span class="p">:</span> <span class="s2">&quot;SOCIAL SECURITY NUMBER&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;display_name&quot;</span><span class="p">:</span> <span class="s2">&quot;NONE&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">],</span>
                <span class="p">},</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">force_delete</span><span class="o">=</span><span class="s2">&quot;false&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-central1&quot;</span><span class="p">,</span>
    <span class="n">tag_template_id</span><span class="o">=</span><span class="s2">&quot;my_template&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for this template.</p></li>
<li><p><strong>fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of tag template field IDs and the settings for the field. This set is an exhaustive list of the allowed fields. This set must contain at least one field and at most 500 fields.  Structure is documented below.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This confirms the deletion of any possible tags using this template. Must be set to true in order to delete the tag template.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Template location region.</p></li>
<li><p><strong>tag_template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the tag template to create.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name for this template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether this is a required field. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The order of this field with respect to other fields in this tag template.
A higher value indicates a more important field. The value can be negative.
Multiple fields can have the same order, and field orders within a tag do not have to be sequential.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The type of value this tag field can contain.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enumType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Represents an enum type.
Exactly one of <code class="docutils literal notranslate"><span class="pre">primitive_type</span></code> or <code class="docutils literal notranslate"><span class="pre">enum_type</span></code> must be set  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of allowed values for this enum. The display names of the
values must be case-insensitively unique within this set. Currently,
enum values can only be added to the list of allowed values. Deletion
and renaming of enum values are not supported.
Can have up to 500 allowed values.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name for this template.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">primitiveType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents primitive types - string, bool etc.
Exactly one of <code class="docutils literal notranslate"><span class="pre">primitive_type</span></code> or <code class="docutils literal notranslate"><span class="pre">enum_type</span></code> must be set</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.TagTemplate.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for this template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.TagTemplate.fields">
<code class="sig-name descname">fields</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.fields" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of tag template field IDs and the settings for the field. This set is an exhaustive list of the allowed fields. This set must contain at least one field and at most 500 fields.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name for this template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether this is a required field. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The order of this field with respect to other fields in this tag template.
A higher value indicates a more important field. The value can be negative.
Multiple fields can have the same order, and field orders within a tag do not have to be sequential.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The type of value this tag field can contain.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enumType</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Represents an enum type.
Exactly one of <code class="docutils literal notranslate"><span class="pre">primitive_type</span></code> or <code class="docutils literal notranslate"><span class="pre">enum_type</span></code> must be set  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of allowed values for this enum. The display names of the
values must be case-insensitively unique within this set. Currently,
enum values can only be added to the list of allowed values. Deletion
and renaming of enum values are not supported.
Can have up to 500 allowed values.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name for this template.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">primitiveType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Represents primitive types - string, bool etc.
Exactly one of <code class="docutils literal notranslate"><span class="pre">primitive_type</span></code> or <code class="docutils literal notranslate"><span class="pre">enum_type</span></code> must be set</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.TagTemplate.force_delete">
<code class="sig-name descname">force_delete</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>This confirms the deletion of any possible tags using this template. Must be set to true in order to delete the tag template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.TagTemplate.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li></li>
</ul>
<p>The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.TagTemplate.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.TagTemplate.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Template location region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.datacatalog.TagTemplate.tag_template_id">
<code class="sig-name descname">tag_template_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.tag_template_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the tag template to create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.TagTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_template_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TagTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for this template.</p></li>
<li><p><strong>fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of tag template field IDs and the settings for the field. This set is an exhaustive list of the allowed fields. This set must contain at least one field and at most 500 fields.  Structure is documented below.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This confirms the deletion of any possible tags using this template. Must be set to true in order to delete the tag template.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li></li>
</ul>
<p>The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Template location region.</p></li>
<li><p><strong>tag_template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the tag template to create.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name for this template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether this is a required field. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The order of this field with respect to other fields in this tag template.
A higher value indicates a more important field. The value can be negative.
Multiple fields can have the same order, and field orders within a tag do not have to be sequential.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The type of value this tag field can contain.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enumType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Represents an enum type.
Exactly one of <code class="docutils literal notranslate"><span class="pre">primitive_type</span></code> or <code class="docutils literal notranslate"><span class="pre">enum_type</span></code> must be set  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of allowed values for this enum. The display names of the
values must be case-insensitively unique within this set. Currently,
enum values can only be added to the list of allowed values. Deletion
and renaming of enum values are not supported.
Can have up to 500 allowed values.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name for this template.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">primitiveType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents primitive types - string, bool etc.
Exactly one of <code class="docutils literal notranslate"><span class="pre">primitive_type</span></code> or <code class="docutils literal notranslate"><span class="pre">enum_type</span></code> must be set</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.datacatalog.TagTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.datacatalog.TagTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.datacatalog.TagTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
