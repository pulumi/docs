---
title: Module database
---

<div class="section" id="database">
<h1>database<a class="headerlink" href="#database" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_openstack.database"></span><dl class="class">
<dt id="pulumi_openstack.database.Configuration">
<em class="property">class </em><code class="descclassname">pulumi_openstack.database.</code><code class="descname">Configuration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>configurations=None</em>, <em>datastore=None</em>, <em>description=None</em>, <em>name=None</em>, <em>region=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 DB configuration resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.</li>
<li><strong>datastore</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An array of database engine type and version. The datastore
object structure is documented below. Changing this creates resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the db instance. Changing this
creates a new instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_configuration_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_configuration_v1.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.database.Configuration.configurations">
<code class="descname">configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Configuration.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Configuration.datastore">
<code class="descname">datastore</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Configuration.datastore" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of database engine type and version. The datastore
object structure is documented below. Changing this creates resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Configuration.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Configuration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Configuration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Configuration.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Configuration.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the db instance. Changing this
creates a new instance.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_openstack.database.Configuration.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>configurations=None</em>, <em>datastore=None</em>, <em>description=None</em>, <em>name=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Configuration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Configuration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] configurations: An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
:param pulumi.Input[dict] datastore: An array of database engine type and version. The datastore</p>
<blockquote>
<div>object structure is documented below. Changing this creates resource.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the db instance. Changing this
creates a new instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_configuration_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_configuration_v1.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.database.Configuration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.database.Configuration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.database.Database">
<em class="property">class </em><code class="descclassname">pulumi_openstack.database.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>instance_id=None</em>, <em>name=None</em>, <em>region=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 DB database resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the database instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Openstack region resource is created in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_database_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_database_v1.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.database.Database.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Database.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the database instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Database.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Database.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Openstack region resource is created in.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_openstack.database.Database.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>instance_id=None</em>, <em>name=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] instance_id: The ID for the database instance.
:param pulumi.Input[str] name: A unique name for the resource.
:param pulumi.Input[str] region: Openstack region resource is created in.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_database_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_database_v1.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.database.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.database.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.database.Instance">
<em class="property">class </em><code class="descclassname">pulumi_openstack.database.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>configuration_id=None</em>, <em>databases=None</em>, <em>datastore=None</em>, <em>flavor_id=None</em>, <em>name=None</em>, <em>networks=None</em>, <em>region=None</em>, <em>size=None</em>, <em>users=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 DB instance resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>configuration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration ID to be attached to the instance. Database instance
will be rebooted when configuration is detached.</li>
<li><strong>databases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of database name, charset and collate. The database
object structure is documented below.</li>
<li><strong>datastore</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An array of database engine type and version. The datastore
object structure is documented below. Changing this creates a new instance.</li>
<li><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The flavor ID of the desired flavor for the instance.
Changing this creates new instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource.</li>
<li><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new instance.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the db instance. Changing this
creates a new instance.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the volume size in GB. Changing this creates new instance.</li>
<li><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of username, password, host and databases. The user
object structure is documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_instance_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_instance_v1.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.configuration_id">
<code class="descname">configuration_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.configuration_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration ID to be attached to the instance. Database instance
will be rebooted when configuration is detached.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.databases">
<code class="descname">databases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.databases" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of database name, charset and collate. The database
object structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.datastore">
<code class="descname">datastore</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.datastore" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of database engine type and version. The datastore
object structure is documented below. Changing this creates a new instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.flavor_id">
<code class="descname">flavor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.flavor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The flavor ID of the desired flavor for the instance.
Changing this creates new instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.networks">
<code class="descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the db instance. Changing this
creates a new instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the volume size in GB. Changing this creates new instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.Instance.users">
<code class="descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.Instance.users" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of username, password, host and databases. The user
object structure is documented below.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_openstack.database.Instance.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>configuration_id=None</em>, <em>databases=None</em>, <em>datastore=None</em>, <em>flavor_id=None</em>, <em>name=None</em>, <em>networks=None</em>, <em>region=None</em>, <em>size=None</em>, <em>users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] configuration_id: Configuration ID to be attached to the instance. Database instance</p>
<blockquote>
<div>will be rebooted when configuration is detached.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>databases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of database name, charset and collate. The database
object structure is documented below.</li>
<li><strong>datastore</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An array of database engine type and version. The datastore
object structure is documented below. Changing this creates a new instance.</li>
<li><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The flavor ID of the desired flavor for the instance.
Changing this creates new instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource.</li>
<li><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new instance.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the db instance. Changing this
creates a new instance.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the volume size in GB. Changing this creates new instance.</li>
<li><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of username, password, host and databases. The user
object structure is documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_instance_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_instance_v1.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.database.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.database.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.database.User">
<em class="property">class </em><code class="descclassname">pulumi_openstack.database.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>databases=None</em>, <em>host=None</em>, <em>instance_id=None</em>, <em>name=None</em>, <em>password=None</em>, <em>region=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 DB user resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>databases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of database user should have access to.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User’s password.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Openstack region resource is created in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_user_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_user_v1.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.database.User.databases">
<code class="descname">databases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.User.databases" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of database user should have access to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.User.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.User.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s password.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.database.User.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.database.User.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Openstack region resource is created in.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_openstack.database.User.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>databases=None</em>, <em>host=None</em>, <em>instance_id=None</em>, <em>name=None</em>, <em>password=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] databases: A list of database user should have access to.
:param pulumi.Input[str] name: A unique name for the resource.
:param pulumi.Input[str] password: User’s password.
:param pulumi.Input[str] region: Openstack region resource is created in.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_user_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_user_v1.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.database.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.database.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.database.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
