---
title: Module bigquery
---

<div class="section" id="bigquery">
<h1>bigquery<a class="headerlink" href="#bigquery" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.bigquery"></span><dl class="class">
<dt id="pulumi_gcp.bigquery.Dataset">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">Dataset</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accesses=None</em>, <em class="sig-param">dataset_id=None</em>, <em class="sig-param">default_partition_expiration_ms=None</em>, <em class="sig-param">default_table_expiration_ms=None</em>, <em class="sig-param">delete_contents_on_destroy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a dataset resource for Google BigQuery. For more information see
<a class="reference external" href="https://cloud.google.com/bigquery/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accesses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of objects that define dataset access for
one or more entities. Structure is documented below.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dataset containing this table.</p></li>
<li><p><strong>default_partition_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default partition expiration
for all partitioned tables in the dataset, in milliseconds.</p></li>
<li><p><strong>default_table_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).</p></li>
<li><p><strong>delete_contents_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the
tables in the dataset when destroying the resource; otherwise, destroying
the resource will fail if tables are present.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly description of the dataset.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the dataset.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_dataset.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_dataset.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.accesses">
<code class="sig-name descname">accesses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of objects that define dataset access for
one or more entities. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.creation_time">
<code class="sig-name descname">creation_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this dataset was created, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.dataset_id">
<code class="sig-name descname">dataset_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dataset containing this table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.default_partition_expiration_ms">
<code class="sig-name descname">default_partition_expiration_ms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.default_partition_expiration_ms" title="Permalink to this definition">¶</a></dt>
<dd><p>The default partition expiration
for all partitioned tables in the dataset, in milliseconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.default_table_expiration_ms">
<code class="sig-name descname">default_table_expiration_ms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.default_table_expiration_ms" title="Permalink to this definition">¶</a></dt>
<dd><p>The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.delete_contents_on_destroy">
<code class="sig-name descname">delete_contents_on_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.delete_contents_on_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the
tables in the dataset when destroying the resource; otherwise, destroying
the resource will fail if tables are present.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-friendly description of the dataset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>A hash of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive name for the dataset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of labels to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.last_modified_time">
<code class="sig-name descname">last_modified_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when this dataset or any of its tables was last modified,
in milliseconds since the epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Dataset.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigquery.Dataset.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accesses=None</em>, <em class="sig-param">creation_time=None</em>, <em class="sig-param">dataset_id=None</em>, <em class="sig-param">default_partition_expiration_ms=None</em>, <em class="sig-param">default_table_expiration_ms=None</em>, <em class="sig-param">delete_contents_on_destroy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">last_modified_time=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dataset resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] accesses: An array of objects that define dataset access for</p>
<blockquote>
<div><p>one or more entities. Structure is documented below.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>creation_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this dataset was created, in milliseconds since the epoch.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dataset containing this table.</p></li>
<li><p><strong>default_partition_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default partition expiration
for all partitioned tables in the dataset, in milliseconds.</p></li>
<li><p><strong>default_table_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).</p></li>
<li><p><strong>delete_contents_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the
tables in the dataset when destroying the resource; otherwise, destroying
the resource will fail if tables are present.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly description of the dataset.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A hash of the resource.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the dataset.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</p></li>
<li><p><strong>last_modified_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The date when this dataset or any of its tables was last modified,
in milliseconds since the epoch.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_dataset.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_dataset.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigquery.Dataset.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.bigquery.Dataset.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.bigquery.Table">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">Table</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dataset_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expiration_time=None</em>, <em class="sig-param">external_data_configuration=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">table_id=None</em>, <em class="sig-param">time_partitioning=None</em>, <em class="sig-param">view=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a table resource in a dataset for Google BigQuery. For more information see
<a class="reference external" href="https://cloud.google.com/bigquery/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID to create the table in.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field description.</p></li>
<li><p><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</p></li>
<li><p><strong>external_data_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the table.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.</p></li>
<li><p><strong>table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique ID for the resource.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures time-based
partitioning for this table. Structure is documented below.</p></li>
<li><p><strong>view</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures this table as a view.
Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.creation_time">
<code class="sig-name descname">creation_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table was created, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.dataset_id">
<code class="sig-name descname">dataset_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The dataset ID to create the table in.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The field description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>A hash of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.expiration_time">
<code class="sig-name descname">expiration_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.external_data_configuration">
<code class="sig-name descname">external_data_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.external_data_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive name for the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of labels to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.last_modified_time">
<code class="sig-name descname">last_modified_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table was last modified, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location where the table resides. This value is inherited from the dataset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.num_bytes">
<code class="sig-name descname">num_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of this table in bytes, excluding any data in the streaming buffer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.num_long_term_bytes">
<code class="sig-name descname">num_long_term_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_long_term_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bytes in the table that are considered “long-term storage”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.num_rows">
<code class="sig-name descname">num_rows</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_rows" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of rows of data in this table, excluding any data in the streaming buffer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.table_id">
<code class="sig-name descname">table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID for the resource.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.time_partitioning">
<code class="sig-name descname">time_partitioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.time_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, configures time-based
partitioning for this table. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the table type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigquery.Table.view">
<code class="sig-name descname">view</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.view" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, configures this table as a view.
Structure is documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigquery.Table.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_time=None</em>, <em class="sig-param">dataset_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">expiration_time=None</em>, <em class="sig-param">external_data_configuration=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">last_modified_time=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">num_bytes=None</em>, <em class="sig-param">num_long_term_bytes=None</em>, <em class="sig-param">num_rows=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">table_id=None</em>, <em class="sig-param">time_partitioning=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">view=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Table resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] creation_time: The time when this table was created, in milliseconds since the epoch.
:param pulumi.Input[str] dataset_id: The dataset ID to create the table in.</p>
<blockquote>
<div><p>Changing this forces a new resource to be created.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field description.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A hash of the resource.</p></li>
<li><p><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</p></li>
<li><p><strong>external_data_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the table.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</p></li>
<li><p><strong>last_modified_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table was last modified, in milliseconds since the epoch.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the table resides. This value is inherited from the dataset.</p></li>
<li><p><strong>num_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of this table in bytes, excluding any data in the streaming buffer.</p></li>
<li><p><strong>num_long_term_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bytes in the table that are considered “long-term storage”.</p></li>
<li><p><strong>num_rows</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of rows of data in this table, excluding any data in the streaming buffer.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.</p>
</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique ID for the resource.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures time-based
partitioning for this table. Structure is documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the table type.</p></li>
<li><p><strong>view</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures this table as a view.
Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigquery.Table.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.bigquery.Table.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
