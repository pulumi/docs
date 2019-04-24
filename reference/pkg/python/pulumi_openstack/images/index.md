<div class="section" id="module-pulumi_openstack.images">
<span id="images"></span><h1>images<a class="headerlink" href="#module-pulumi_openstack.images" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_openstack.images.GetImageResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.images.</code><code class="descname">GetImageResult</code><span class="sig-paren">(</span><em>checksum=None</em>, <em>container_format=None</em>, <em>created_at=None</em>, <em>disk_format=None</em>, <em>file=None</em>, <em>member_status=None</em>, <em>metadata=None</em>, <em>min_disk_gb=None</em>, <em>min_ram_mb=None</em>, <em>most_recent=None</em>, <em>name=None</em>, <em>owner=None</em>, <em>properties=None</em>, <em>protected=None</em>, <em>region=None</em>, <em>schema=None</em>, <em>size_bytes=None</em>, <em>size_max=None</em>, <em>size_min=None</em>, <em>sort_direction=None</em>, <em>sort_key=None</em>, <em>tag=None</em>, <em>tags=None</em>, <em>updated_at=None</em>, <em>visibility=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.checksum">
<code class="descname">checksum</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>The checksum of the data associated with the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image was created.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">container_format</span></code>: The format of the image’s container.</li>
<li><code class="docutils literal notranslate"><span class="pre">disk_format</span></code>: The format of the image’s disk.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.file">
<code class="descname">file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.file" title="Permalink to this definition">¶</a></dt>
<dd><p>the trailing path after the glance endpoint that represent the
location of the image or the path to retrieve it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata associated with the image.
Image metadata allow for meaningfully define the image properties
and tags. See <a class="reference external" href="https://docs.openstack.org/glance/latest/user/metadefs-concepts.html">https://docs.openstack.org/glance/latest/user/metadefs-concepts.html</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.min_disk_gb">
<code class="descname">min_disk_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.min_disk_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum amount of disk space required to use the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.min_ram_mb">
<code class="descname">min_ram_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.min_ram_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum amount of ram required to use the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.properties">
<code class="descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Freeform information about the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.protected">
<code class="descname">protected</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.protected" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the image is protected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the JSON-schema that represent
the image or image</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.size_bytes">
<code class="descname">size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the image (in bytes).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags list of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.updated_at">
<code class="descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.images.Image">
<em class="property">class </em><code class="descclassname">pulumi_openstack.images.</code><code class="descname">Image</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>container_format=None</em>, <em>disk_format=None</em>, <em>image_cache_path=None</em>, <em>image_source_url=None</em>, <em>local_file_path=None</em>, <em>min_disk_gb=None</em>, <em>min_ram_mb=None</em>, <em>name=None</em>, <em>properties=None</em>, <em>protected=None</em>, <em>region=None</em>, <em>tags=None</em>, <em>verify_checksum=None</em>, <em>visibility=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Image resource within OpenStack Glance.</p>
<p>This resource supports the ability to add properties to a resource during
creation as well as add, update, and delete properties during an update of this
resource.</p>
<p>Newer versions of OpenStack are adding some read-only properties to each image.
These properties start with the prefix <code class="docutils literal notranslate"><span class="pre">os_</span></code>. If these properties are detected,
this resource will automatically reconcile these with the user-provided
properties.</p>
<p>In addition, the <code class="docutils literal notranslate"><span class="pre">direct_url</span></code> property is also automatically reconciled if the
Image Service set it.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>container_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container format. Must be one of
“ami”, “ari”, “aki”, “bare”, “ovf”.</li>
<li><strong>disk_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The disk format. Must be one of
“ami”, “ari”, “aki”, “vhd”, “vmdk”, “raw”, “qcow2”, “vdi”, “iso”.</li>
<li><strong>image_cache_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the directory where the images will
be downloaded. Images will be stored with a filename corresponding to
the url’s md5 hash. Defaults to “$HOME/.terraform/image_cache”</li>
<li><strong>image_source_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the url of the raw image that will
be downloaded in the <code class="docutils literal notranslate"><span class="pre">image_cache_path</span></code> before being uploaded to Glance.
Glance is able to download image from internet but the <code class="docutils literal notranslate"><span class="pre">gophercloud</span></code> library
does not yet provide a way to do so.
Conflicts with <code class="docutils literal notranslate"><span class="pre">local_file_path</span></code>.</li>
<li><strong>local_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with <code class="docutils literal notranslate"><span class="pre">image_source_url</span></code>.</li>
<li><strong>min_disk_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of disk space (in GB) required to boot image.
Defaults to 0.</li>
<li><strong>min_ram_mb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of ram (in MB) required to boot image.
Defauts to 0.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the image.</li>
<li><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key/value pairs to set freeform
information about an image. See the “Notes” section for further
information about properties.</li>
<li><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, image will not be deletable.
Defaults to false.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new Image.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.</li>
<li><strong>verify_checksum</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If false, the checksum will not be verified
once the image is finished uploading. Defaults to true.</li>
<li><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The visibility of the image. Must be one of
“public”, “private”, “community”, or “shared”. The ability to set the
visibility depends upon the configuration of the OpenStack cloud.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.images.Image.checksum">
<code class="descname">checksum</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>The checksum of the data associated with the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.container_format">
<code class="descname">container_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.container_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The container format. Must be one of
“ami”, “ari”, “aki”, “bare”, “ovf”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.disk_format">
<code class="descname">disk_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.disk_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The disk format. Must be one of
“ami”, “ari”, “aki”, “vhd”, “vmdk”, “raw”, “qcow2”, “vdi”, “iso”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.file">
<code class="descname">file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.file" title="Permalink to this definition">¶</a></dt>
<dd><p>the trailing path after the glance
endpoint that represent the location of the image
or the path to retrieve it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.image_cache_path">
<code class="descname">image_cache_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.image_cache_path" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the directory where the images will
be downloaded. Images will be stored with a filename corresponding to
the url’s md5 hash. Defaults to “$HOME/.terraform/image_cache”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.image_source_url">
<code class="descname">image_source_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.image_source_url" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the url of the raw image that will
be downloaded in the <code class="docutils literal notranslate"><span class="pre">image_cache_path</span></code> before being uploaded to Glance.
Glance is able to download image from internet but the <code class="docutils literal notranslate"><span class="pre">gophercloud</span></code> library
does not yet provide a way to do so.
Conflicts with <code class="docutils literal notranslate"><span class="pre">local_file_path</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.local_file_path">
<code class="descname">local_file_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.local_file_path" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with <code class="docutils literal notranslate"><span class="pre">image_source_url</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata associated with the image.
Image metadata allow for meaningfully define the image properties
and tags. See <a class="reference external" href="https://docs.openstack.org/glance/latest/user/metadefs-concepts.html">https://docs.openstack.org/glance/latest/user/metadefs-concepts.html</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.min_disk_gb">
<code class="descname">min_disk_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.min_disk_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of disk space (in GB) required to boot image.
Defaults to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.min_ram_mb">
<code class="descname">min_ram_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.min_ram_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of ram (in MB) required to boot image.
Defauts to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.owner">
<code class="descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the openstack user who owns the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.properties">
<code class="descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of key/value pairs to set freeform
information about an image. See the “Notes” section for further
information about properties.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.protected">
<code class="descname">protected</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.protected" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, image will not be deletable.
Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the JSON-schema that represent
the image or image</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.size_bytes">
<code class="descname">size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in bytes of the data associated with the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the image. It can be “queued”, “active”
or “saving”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.update_at">
<code class="descname">update_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.update_at" title="Permalink to this definition">¶</a></dt>
<dd><p>(<strong>Deprecated</strong> - use <code class="docutils literal notranslate"><span class="pre">updated_at</span></code> instead)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.updated_at">
<code class="descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.verify_checksum">
<code class="descname">verify_checksum</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.verify_checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>If false, the checksum will not be verified
once the image is finished uploading. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.visibility">
<code class="descname">visibility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>The visibility of the image. Must be one of
“public”, “private”, “community”, or “shared”. The ability to set the
visibility depends upon the configuration of the OpenStack cloud.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.images.Image.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.images.Image.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.images.get_image">
<code class="descclassname">pulumi_openstack.images.</code><code class="descname">get_image</code><span class="sig-paren">(</span><em>member_status=None</em>, <em>most_recent=None</em>, <em>name=None</em>, <em>owner=None</em>, <em>properties=None</em>, <em>region=None</em>, <em>size_max=None</em>, <em>size_min=None</em>, <em>sort_direction=None</em>, <em>sort_key=None</em>, <em>tag=None</em>, <em>visibility=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack image.</p>
</dd></dl>

</div>
