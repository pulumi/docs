---
title: Module images
title_tag: Module images | Package pulumi_openstack | Python SDK
linktitle: images
notitle: true
---

<div class="section" id="images">
<h1>images<a class="headerlink" href="#images" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.images"></span><dl class="class">
<dt id="pulumi_openstack.images.AwaitableGetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.images.</code><code class="sig-name descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em class="sig-param">checksum=None</em>, <em class="sig-param">container_format=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">disk_format=None</em>, <em class="sig-param">file=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">member_status=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">min_disk_gb=None</em>, <em class="sig-param">min_ram_mb=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">protected=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">size_bytes=None</em>, <em class="sig-param">size_max=None</em>, <em class="sig-param">size_min=None</em>, <em class="sig-param">sort_direction=None</em>, <em class="sig-param">sort_key=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">visibility=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.images.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.images.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param">checksum=None</em>, <em class="sig-param">container_format=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">disk_format=None</em>, <em class="sig-param">file=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">member_status=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">min_disk_gb=None</em>, <em class="sig-param">min_ram_mb=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">protected=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">size_bytes=None</em>, <em class="sig-param">size_max=None</em>, <em class="sig-param">size_min=None</em>, <em class="sig-param">sort_direction=None</em>, <em class="sig-param">sort_key=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">visibility=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.checksum">
<code class="sig-name descname">checksum</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>The checksum of the data associated with the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image was created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">container_format</span></code>: The format of the image’s container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_format</span></code>: The format of the image’s disk.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.file">
<code class="sig-name descname">file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.file" title="Permalink to this definition">¶</a></dt>
<dd><p>the trailing path after the glance endpoint that represent the
location of the image or the path to retrieve it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata associated with the image.
Image metadata allow for meaningfully define the image properties
and tags. See <a class="reference external" href="https://docs.openstack.org/glance/latest/user/metadefs-concepts.html">https://docs.openstack.org/glance/latest/user/metadefs-concepts.html</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.min_disk_gb">
<code class="sig-name descname">min_disk_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.min_disk_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum amount of disk space required to use the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.min_ram_mb">
<code class="sig-name descname">min_ram_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.min_ram_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum amount of ram required to use the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.properties">
<code class="sig-name descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Freeform information about the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.protected">
<code class="sig-name descname">protected</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.protected" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the image is protected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the JSON-schema that represent
the image or image</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.size_bytes">
<code class="sig-name descname">size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the image (in bytes).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags list of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.GetImageResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.GetImageResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image was last updated.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.images.Image">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.images.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">container_format=None</em>, <em class="sig-param">disk_format=None</em>, <em class="sig-param">image_cache_path=None</em>, <em class="sig-param">image_source_url=None</em>, <em class="sig-param">local_file_path=None</em>, <em class="sig-param">min_disk_gb=None</em>, <em class="sig-param">min_ram_mb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">protected=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">verify_checksum=None</em>, <em class="sig-param">visibility=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.Image" title="Permalink to this definition">¶</a></dt>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container format. Must be one of
“ami”, “ari”, “aki”, “bare”, “ovf”.</p></li>
<li><p><strong>disk_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The disk format. Must be one of
“ami”, “ari”, “aki”, “vhd”, “vmdk”, “raw”, “qcow2”, “vdi”, “iso”.</p></li>
<li><p><strong>image_source_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the url of the raw image that will
be downloaded in the <code class="docutils literal notranslate"><span class="pre">image_cache_path</span></code> before being uploaded to Glance.
Glance is able to download image from internet but the <code class="docutils literal notranslate"><span class="pre">gophercloud</span></code> library
does not yet provide a way to do so.
Conflicts with <code class="docutils literal notranslate"><span class="pre">local_file_path</span></code>.</p></li>
<li><p><strong>local_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with <code class="docutils literal notranslate"><span class="pre">image_source_url</span></code>.</p></li>
<li><p><strong>min_disk_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of disk space (in GB) required to boot image.
Defaults to 0.</p></li>
<li><p><strong>min_ram_mb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of ram (in MB) required to boot image.
Defauts to 0.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the image.</p></li>
<li><p><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key/value pairs to set freeform
information about an image. See the “Notes” section for further
information about properties.</p></li>
<li><p><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, image will not be deletable.
Defaults to false.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new Image.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.</p></li>
<li><p><strong>verify_checksum</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If false, the checksum will not be verified
once the image is finished uploading. Defaults to true.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The visibility of the image. Must be one of
“public”, “private”, “community”, or “shared”. The ability to set the
visibility depends upon the configuration of the OpenStack cloud.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.images.Image.checksum">
<code class="sig-name descname">checksum</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>The checksum of the data associated with the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.container_format">
<code class="sig-name descname">container_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.container_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The container format. Must be one of
“ami”, “ari”, “aki”, “bare”, “ovf”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.disk_format">
<code class="sig-name descname">disk_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.disk_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The disk format. Must be one of
“ami”, “ari”, “aki”, “vhd”, “vmdk”, “raw”, “qcow2”, “vdi”, “iso”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.file">
<code class="sig-name descname">file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.file" title="Permalink to this definition">¶</a></dt>
<dd><p>the trailing path after the glance
endpoint that represent the location of the image
or the path to retrieve it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.image_source_url">
<code class="sig-name descname">image_source_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.image_source_url" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the url of the raw image that will
be downloaded in the <code class="docutils literal notranslate"><span class="pre">image_cache_path</span></code> before being uploaded to Glance.
Glance is able to download image from internet but the <code class="docutils literal notranslate"><span class="pre">gophercloud</span></code> library
does not yet provide a way to do so.
Conflicts with <code class="docutils literal notranslate"><span class="pre">local_file_path</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.local_file_path">
<code class="sig-name descname">local_file_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.local_file_path" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with <code class="docutils literal notranslate"><span class="pre">image_source_url</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata associated with the image.
Image metadata allow for meaningfully define the image properties
and tags. See <a class="reference external" href="https://docs.openstack.org/glance/latest/user/metadefs-concepts.html">https://docs.openstack.org/glance/latest/user/metadefs-concepts.html</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.min_disk_gb">
<code class="sig-name descname">min_disk_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.min_disk_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of disk space (in GB) required to boot image.
Defaults to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.min_ram_mb">
<code class="sig-name descname">min_ram_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.min_ram_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of ram (in MB) required to boot image.
Defauts to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the openstack user who owns the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.properties">
<code class="sig-name descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of key/value pairs to set freeform
information about an image. See the “Notes” section for further
information about properties.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.protected">
<code class="sig-name descname">protected</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.protected" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, image will not be deletable.
Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the JSON-schema that represent
the image or image</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.size_bytes">
<code class="sig-name descname">size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in bytes of the data associated with the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the image. It can be “queued”, “active”
or “saving”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.update_at">
<code class="sig-name descname">update_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.update_at" title="Permalink to this definition">¶</a></dt>
<dd><p>(<strong>Deprecated</strong> - use <code class="docutils literal notranslate"><span class="pre">updated_at</span></code> instead)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.verify_checksum">
<code class="sig-name descname">verify_checksum</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.verify_checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>If false, the checksum will not be verified
once the image is finished uploading. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.Image.visibility">
<code class="sig-name descname">visibility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.Image.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>The visibility of the image. Must be one of
“public”, “private”, “community”, or “shared”. The ability to set the
visibility depends upon the configuration of the OpenStack cloud.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.images.Image.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">checksum=None</em>, <em class="sig-param">container_format=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">disk_format=None</em>, <em class="sig-param">file=None</em>, <em class="sig-param">image_cache_path=None</em>, <em class="sig-param">image_source_url=None</em>, <em class="sig-param">local_file_path=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">min_disk_gb=None</em>, <em class="sig-param">min_ram_mb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">protected=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">size_bytes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">update_at=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">verify_checksum=None</em>, <em class="sig-param">visibility=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.Image.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Image resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>checksum</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The checksum of the data associated with the image.</p></li>
<li><p><strong>container_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container format. Must be one of
“ami”, “ari”, “aki”, “bare”, “ovf”.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the image was created.</p></li>
<li><p><strong>disk_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The disk format. Must be one of
“ami”, “ari”, “aki”, “vhd”, “vmdk”, “raw”, “qcow2”, “vdi”, “iso”.</p></li>
<li><p><strong>file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the trailing path after the glance
endpoint that represent the location of the image
or the path to retrieve it.</p></li>
<li><p><strong>image_source_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the url of the raw image that will
be downloaded in the <code class="docutils literal notranslate"><span class="pre">image_cache_path</span></code> before being uploaded to Glance.
Glance is able to download image from internet but the <code class="docutils literal notranslate"><span class="pre">gophercloud</span></code> library
does not yet provide a way to do so.
Conflicts with <code class="docutils literal notranslate"><span class="pre">local_file_path</span></code>.</p></li>
<li><p><strong>local_file_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with <code class="docutils literal notranslate"><span class="pre">image_source_url</span></code>.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The metadata associated with the image.
Image metadata allow for meaningfully define the image properties
and tags. See <a class="reference external" href="https://docs.openstack.org/glance/latest/user/metadefs-concepts.html">https://docs.openstack.org/glance/latest/user/metadefs-concepts.html</a>.</p></li>
<li><p><strong>min_disk_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of disk space (in GB) required to boot image.
Defaults to 0.</p></li>
<li><p><strong>min_ram_mb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of ram (in MB) required to boot image.
Defauts to 0.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the image.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the openstack user who owns the image.</p></li>
<li><p><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key/value pairs to set freeform
information about an image. See the “Notes” section for further
information about properties.</p></li>
<li><p><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, image will not be deletable.
Defaults to false.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new Image.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the JSON-schema that represent
the image or image</p></li>
<li><p><strong>size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size in bytes of the data associated with the image.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the image. It can be “queued”, “active”
or “saving”.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.</p></li>
<li><p><strong>update_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (<strong>Deprecated</strong> - use <code class="docutils literal notranslate"><span class="pre">updated_at</span></code> instead)</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the image was last updated.</p></li>
<li><p><strong>verify_checksum</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If false, the checksum will not be verified
once the image is finished uploading. Defaults to true.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The visibility of the image. Must be one of
“public”, “private”, “community”, or “shared”. The ability to set the
visibility depends upon the configuration of the OpenStack cloud.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.images.Image.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.images.Image.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.images.ImageAccess">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.images.</code><code class="sig-name descname">ImageAccess</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">member_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.ImageAccess" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages members for the shared OpenStack Glance V2 Image within the source
project, which owns the Image.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID.</p></li>
<li><p><strong>member_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The member ID, e.g. the target project ID.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Glance client.
A Glance client is needed to manage Image members. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code>
argument of the provider is used. Changing this creates a new resource.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The member proposal status. Optional if admin wants to
force the member proposal acceptance. Can either be <code class="docutils literal notranslate"><span class="pre">accepted</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code> or
<code class="docutils literal notranslate"><span class="pre">pending</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending</span></code>. Foridden for non-admin users.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccess.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image access was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccess.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The image ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccess.member_id">
<code class="sig-name descname">member_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.member_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The member ID, e.g. the target project ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccess.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Glance client.
A Glance client is needed to manage Image members. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code>
argument of the provider is used. Changing this creates a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccess.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The member schema.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccess.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The member proposal status. Optional if admin wants to
force the member proposal acceptance. Can either be <code class="docutils literal notranslate"><span class="pre">accepted</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code> or
<code class="docutils literal notranslate"><span class="pre">pending</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending</span></code>. Foridden for non-admin users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccess.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image access was last updated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.images.ImageAccess.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">member_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ImageAccess resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the image access was created.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID.</p></li>
<li><p><strong>member_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The member ID, e.g. the target project ID.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Glance client.
A Glance client is needed to manage Image members. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code>
argument of the provider is used. Changing this creates a new resource.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The member schema.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The member proposal status. Optional if admin wants to
force the member proposal acceptance. Can either be <code class="docutils literal notranslate"><span class="pre">accepted</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code> or
<code class="docutils literal notranslate"><span class="pre">pending</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pending</span></code>. Foridden for non-admin users.</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the image access was last updated.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.images.ImageAccess.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.images.ImageAccess.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.ImageAccess.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.images.ImageAccessAccept">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.images.</code><code class="sig-name descname">ImageAccessAccept</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">member_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages memberships status for the shared OpenStack Glance V2 Image within the
destination project, which has a member proposal.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The proposed image ID.</p></li>
<li><p><strong>member_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The member ID, e.g. the target project ID. Optional
for admin accounts. Defaults to the current scope project ID.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Glance client.
A Glance client is needed to manage Image memberships. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
membership.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The membership proposal status. Can either be
<code class="docutils literal notranslate"><span class="pre">accepted</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code> or <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccessAccept.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image membership was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccessAccept.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The proposed image ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccessAccept.member_id">
<code class="sig-name descname">member_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.member_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The member ID, e.g. the target project ID. Optional
for admin accounts. Defaults to the current scope project ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccessAccept.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Glance client.
A Glance client is needed to manage Image memberships. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
membership.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccessAccept.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The membership schema.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccessAccept.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The membership proposal status. Can either be
<code class="docutils literal notranslate"><span class="pre">accepted</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code> or <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.images.ImageAccessAccept.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the image membership was last updated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.images.ImageAccessAccept.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">member_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ImageAccessAccept resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the image membership was created.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The proposed image ID.</p></li>
<li><p><strong>member_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The member ID, e.g. the target project ID. Optional
for admin accounts. Defaults to the current scope project ID.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Glance client.
A Glance client is needed to manage Image memberships. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
membership.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The membership schema.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The membership proposal status. Can either be
<code class="docutils literal notranslate"><span class="pre">accepted</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code> or <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the image membership was last updated.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.images.ImageAccessAccept.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.images.ImageAccessAccept.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.ImageAccessAccept.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_openstack.images.get_image">
<code class="sig-prename descclassname">pulumi_openstack.images.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param">member_status=None</em>, <em class="sig-param">most_recent=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">size_max=None</em>, <em class="sig-param">size_min=None</em>, <em class="sig-param">sort_direction=None</em>, <em class="sig-param">sort_key=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">visibility=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.images.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack image.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>member_status</strong> (<em>str</em>) – The status of the image. Must be one of
“accepted”, “pending”, “rejected”, or “all”.</p></li>
<li><p><strong>most_recent</strong> (<em>bool</em>) – If more than one result is returned, use the most
recent image.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the image.</p></li>
<li><p><strong>owner</strong> (<em>str</em>) – The owner (UUID) of the image.</p></li>
<li><p><strong>properties</strong> (<em>dict</em>) – a map of key/value pairs to match an image with.
All specified properties must be matched.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used.</p></li>
<li><p><strong>size_max</strong> (<em>float</em>) – The maximum size (in bytes) of the image to return.</p></li>
<li><p><strong>size_min</strong> (<em>float</em>) – The minimum size (in bytes) of the image to return.</p></li>
<li><p><strong>sort_direction</strong> (<em>str</em>) – Order the results in either <code class="docutils literal notranslate"><span class="pre">asc</span></code> or <code class="docutils literal notranslate"><span class="pre">desc</span></code>.</p></li>
<li><p><strong>sort_key</strong> (<em>str</em>) – Sort images based on a certain key. Defaults to <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>tag</strong> (<em>str</em>) – Search for images with a specific tag.</p></li>
<li><p><strong>visibility</strong> (<em>str</em>) – The visibility of the image. Must be one of
“public”, “private”, “community”, or “shared”. Defaults to “private”.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
