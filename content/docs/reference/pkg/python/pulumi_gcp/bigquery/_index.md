---
title: Module bigquery
---

<div class="section" id="bigquery">
<h1>bigquery<a class="headerlink" href="#bigquery" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.bigquery"></span><dl class="class">
<dt id="pulumi_gcp.bigquery.Dataset">
<em class="property">class </em><code class="descclassname">pulumi_gcp.bigquery.</code><code class="descname">Dataset</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>accesses=None</em>, <em>dataset_id=None</em>, <em>default_partition_expiration_ms=None</em>, <em>default_table_expiration_ms=None</em>, <em>delete_contents_on_destroy=None</em>, <em>description=None</em>, <em>friendly_name=None</em>, <em>labels=None</em>, <em>location=None</em>, <em>project=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a dataset resource for Google BigQuery. For more information see
<a class="reference external" href="https://cloud.google.com/bigquery/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>accesses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of objects that define dataset access for
one or more entities. Structure is documented below.</li>
<li><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dataset containing this table.</li>
<li><strong>default_partition_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default partition expiration
for all partitioned tables in the dataset, in milliseconds.</li>
<li><strong>default_table_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).</li>
<li><strong>delete_contents_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the
tables in the dataset when destroying the resource; otherwise, destroying
the resource will fail if tables are present.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly description of the dataset.</li>
<li><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the dataset.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_dataset.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_dataset.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.accesses">
<code class="descname">accesses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of objects that define dataset access for
one or more entities. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.creation_time">
<code class="descname">creation_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this dataset was created, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.dataset_id">
<code class="descname">dataset_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dataset containing this table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.default_partition_expiration_ms">
<code class="descname">default_partition_expiration_ms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.default_partition_expiration_ms" title="Permalink to this definition">¶</a></dt>
<dd><p>The default partition expiration
for all partitioned tables in the dataset, in milliseconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.default_table_expiration_ms">
<code class="descname">default_table_expiration_ms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.default_table_expiration_ms" title="Permalink to this definition">¶</a></dt>
<dd><p>The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.delete_contents_on_destroy">
<code class="descname">delete_contents_on_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.delete_contents_on_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the
tables in the dataset when destroying the resource; otherwise, destroying
the resource will fail if tables are present.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-friendly description of the dataset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>A hash of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.friendly_name">
<code class="descname">friendly_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive name for the dataset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of labels to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.last_modified_time">
<code class="descname">last_modified_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when this dataset or any of its tables was last modified,
in milliseconds since the epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gcp.bigquery.Dataset.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>accesses=None</em>, <em>creation_time=None</em>, <em>dataset_id=None</em>, <em>default_partition_expiration_ms=None</em>, <em>default_table_expiration_ms=None</em>, <em>delete_contents_on_destroy=None</em>, <em>description=None</em>, <em>etag=None</em>, <em>friendly_name=None</em>, <em>labels=None</em>, <em>last_modified_time=None</em>, <em>location=None</em>, <em>project=None</em>, <em>self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dataset resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] accesses: An array of objects that define dataset access for</p>
<blockquote>
<div>one or more entities. Structure is documented below.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>creation_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this dataset was created, in milliseconds since the epoch.</li>
<li><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dataset containing this table.</li>
<li><strong>default_partition_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default partition expiration
for all partitioned tables in the dataset, in milliseconds.</li>
<li><strong>default_table_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).</li>
<li><strong>delete_contents_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the
tables in the dataset when destroying the resource; otherwise, destroying
the resource will fail if tables are present.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly description of the dataset.</li>
<li><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A hash of the resource.</li>
<li><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the dataset.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</li>
<li><strong>last_modified_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The date when this dataset or any of its tables was last modified,
in milliseconds since the epoch.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</p>
</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_dataset.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_dataset.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigquery.Dataset.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Dataset.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Table">
<em class="property">class </em><code class="descclassname">pulumi_gcp.bigquery.</code><code class="descname">Table</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>dataset_id=None</em>, <em>description=None</em>, <em>expiration_time=None</em>, <em>external_data_configuration=None</em>, <em>friendly_name=None</em>, <em>labels=None</em>, <em>project=None</em>, <em>schema=None</em>, <em>table_id=None</em>, <em>time_partitioning=None</em>, <em>view=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a table resource in a dataset for Google BigQuery. For more information see
<a class="reference external" href="https://cloud.google.com/bigquery/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID to create the table in.
Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field description.</li>
<li><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</li>
<li><strong>external_data_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</li>
<li><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the table.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.</li>
<li><strong>table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique ID for the resource.
Changing this forces a new resource to be created.</li>
<li><strong>time_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures time-based
partitioning for this table. Structure is documented below.</li>
<li><strong>view</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures this table as a view.
Structure is documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.creation_time">
<code class="descname">creation_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table was created, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.dataset_id">
<code class="descname">dataset_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The dataset ID to create the table in.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The field description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>A hash of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.expiration_time">
<code class="descname">expiration_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.external_data_configuration">
<code class="descname">external_data_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.external_data_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.friendly_name">
<code class="descname">friendly_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive name for the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of labels to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.last_modified_time">
<code class="descname">last_modified_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table was last modified, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location where the table resides. This value is inherited from the dataset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.num_bytes">
<code class="descname">num_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of this table in bytes, excluding any data in the streaming buffer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.num_long_term_bytes">
<code class="descname">num_long_term_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_long_term_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bytes in the table that are considered “long-term storage”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.num_rows">
<code class="descname">num_rows</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_rows" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of rows of data in this table, excluding any data in the streaming buffer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.table_id">
<code class="descname">table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID for the resource.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.time_partitioning">
<code class="descname">time_partitioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.time_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, configures time-based
partitioning for this table. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the table type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.view">
<code class="descname">view</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.view" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, configures this table as a view.
Structure is documented below.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gcp.bigquery.Table.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>creation_time=None</em>, <em>dataset_id=None</em>, <em>description=None</em>, <em>etag=None</em>, <em>expiration_time=None</em>, <em>external_data_configuration=None</em>, <em>friendly_name=None</em>, <em>labels=None</em>, <em>last_modified_time=None</em>, <em>location=None</em>, <em>num_bytes=None</em>, <em>num_long_term_bytes=None</em>, <em>num_rows=None</em>, <em>project=None</em>, <em>schema=None</em>, <em>self_link=None</em>, <em>table_id=None</em>, <em>time_partitioning=None</em>, <em>type=None</em>, <em>view=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Table resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] creation_time: The time when this table was created, in milliseconds since the epoch.
:param pulumi.Input[str] dataset_id: The dataset ID to create the table in.</p>
<blockquote>
<div>Changing this forces a new resource to be created.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field description.</li>
<li><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A hash of the resource.</li>
<li><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</li>
<li><strong>external_data_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</li>
<li><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the table.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</li>
<li><strong>last_modified_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table was last modified, in milliseconds since the epoch.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the table resides. This value is inherited from the dataset.</li>
<li><strong>num_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of this table in bytes, excluding any data in the streaming buffer.</li>
<li><strong>num_long_term_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bytes in the table that are considered “long-term storage”.</li>
<li><strong>num_rows</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of rows of data in this table, excluding any data in the streaming buffer.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.</p>
</li>
<li><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</li>
<li><strong>table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique ID for the resource.
Changing this forces a new resource to be created.</li>
<li><strong>time_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures time-based
partitioning for this table. Structure is documented below.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the table type.</li>
<li><strong>view</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures this table as a view.
Structure is documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigquery.Table.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Table.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
