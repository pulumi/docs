<div class="section" id="module-pulumi_openstack.objectstorage">
<span id="objectstorage"></span><h1>objectstorage<a class="headerlink" href="#module-pulumi_openstack.objectstorage" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_openstack.objectstorage.Container">
<em class="property">class </em><code class="descclassname">pulumi_openstack.objectstorage.</code><code class="descname">Container</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>container_read=None</em>, <em>container_sync_key=None</em>, <em>container_sync_to=None</em>, <em>container_write=None</em>, <em>content_type=None</em>, <em>force_destroy=None</em>, <em>metadata=None</em>, <em>name=None</em>, <em>region=None</em>, <em>versioning=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.Container" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 container resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>container_read</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets an access control list (ACL) that grants
read access. This header can contain a comma-delimited list of users that
can read the container (allows the GET method for all objects in the
container). Changing this updates the access control list read access.</li>
<li><strong>container_sync_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret key for container synchronization.
Changing this updates container synchronization.</li>
<li><strong>container_sync_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination for container synchronization.
Changing this updates container synchronization.</li>
<li><strong>container_write</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets an ACL that grants write access.
Changing this updates the access control list write access.</li>
<li><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MIME type for the container. Changing this
updates the MIME type.</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all objects should be deleted from the container so that the container can be destroyed without error. These objects are not recoverable.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Custom key/value pairs to associate with the container.
Changing this updates the existing container metadata.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the container. Changing this creates a
new container.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the container. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new container.</li>
<li><strong>versioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enable object versioning. The structure is described below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.container_read">
<code class="descname">container_read</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.container_read" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets an access control list (ACL) that grants
read access. This header can contain a comma-delimited list of users that
can read the container (allows the GET method for all objects in the
container). Changing this updates the access control list read access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.container_sync_key">
<code class="descname">container_sync_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.container_sync_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret key for container synchronization.
Changing this updates container synchronization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.container_sync_to">
<code class="descname">container_sync_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.container_sync_to" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination for container synchronization.
Changing this updates container synchronization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.container_write">
<code class="descname">container_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.container_write" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets an ACL that grants write access.
Changing this updates the access control list write access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The MIME type for the container. Changing this
updates the MIME type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all objects should be deleted from the container so that the container can be destroyed without error. These objects are not recoverable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom key/value pairs to associate with the container.
Changing this updates the existing container metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the container. Changing this creates a
new container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the container. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.Container.versioning">
<code class="descname">versioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.versioning" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable object versioning. The structure is described below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.objectstorage.Container.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.objectstorage.Container.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.Container.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.objectstorage.ContainerObject">
<em class="property">class </em><code class="descclassname">pulumi_openstack.objectstorage.</code><code class="descname">ContainerObject</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>container_name=None</em>, <em>content=None</em>, <em>content_disposition=None</em>, <em>content_encoding=None</em>, <em>content_type=None</em>, <em>copy_from=None</em>, <em>delete_after=None</em>, <em>delete_at=None</em>, <em>detect_content_type=None</em>, <em>etag=None</em>, <em>metadata=None</em>, <em>name=None</em>, <em>object_manifest=None</em>, <em>region=None</em>, <em>source=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 container object resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.</li>
<li><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the content of the object. Conflicts with
<code class="docutils literal notranslate"><span class="pre">source</span></code> and <code class="docutils literal notranslate"><span class="pre">copy_from</span></code>.</li>
<li><strong>content_disposition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.</li>
<li><strong>content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the value of the Content-Encoding
metadata.</li>
<li><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string which sets the MIME type for the object.</li>
<li><strong>copy_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the name of an object 
used to create the new object by copying the <code class="docutils literal notranslate"><span class="pre">copy_from</span></code> object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with <code class="docutils literal notranslate"><span class="pre">source</span></code> and
<code class="docutils literal notranslate"><span class="pre">content</span></code>.</li>
<li><strong>delete_after</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.</li>
<li><strong>delete_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An string representing the date when the system removes the object. 
For example, “2015-08-26” is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.</li>
<li><strong>detect_content_type</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.</li>
<li><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to trigger updates. The only meaningful value is ${md5(file(“path/to/file”))}.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the object.</li>
<li><strong>object_manifest</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the container. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new container.</li>
<li><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the local path of a file which will be used
as the object’s content. Conflicts with <code class="docutils literal notranslate"><span class="pre">source</span></code> and <code class="docutils literal notranslate"><span class="pre">copy_from</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.container_name">
<code class="descname">container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.content" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the content of the object. Conflicts with
<code class="docutils literal notranslate"><span class="pre">source</span></code> and <code class="docutils literal notranslate"><span class="pre">copy_from</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.content_disposition">
<code class="descname">content_disposition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.content_disposition" title="Permalink to this definition">¶</a></dt>
<dd><p>A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.content_encoding">
<code class="descname">content_encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the value of the Content-Encoding
metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.content_length">
<code class="descname">content_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.content_length" title="Permalink to this definition">¶</a></dt>
<dd><p>If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A string which sets the MIME type for the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.copy_from">
<code class="descname">copy_from</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.copy_from" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the name of an object 
used to create the new object by copying the <code class="docutils literal notranslate"><span class="pre">copy_from</span></code> object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with <code class="docutils literal notranslate"><span class="pre">source</span></code> and
<code class="docutils literal notranslate"><span class="pre">content</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.date">
<code class="descname">date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.delete_after">
<code class="descname">delete_after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.delete_after" title="Permalink to this definition">¶</a></dt>
<dd><p>An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.delete_at">
<code class="descname">delete_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.delete_at" title="Permalink to this definition">¶</a></dt>
<dd><p>An string representing the date when the system removes the object. 
For example, “2015-08-26” is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.detect_content_type">
<code class="descname">detect_content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.detect_content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to trigger updates. The only meaningful value is ${md5(file(“path/to/file”))}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.last_modified">
<code class="descname">last_modified</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.object_manifest">
<code class="descname">object_manifest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.object_manifest" title="Permalink to this definition">¶</a></dt>
<dd><p>A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the container. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.source">
<code class="descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.source" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the local path of a file which will be used
as the object’s content. Conflicts with <code class="docutils literal notranslate"><span class="pre">source</span></code> and <code class="docutils literal notranslate"><span class="pre">copy_from</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.ContainerObject.trans_id">
<code class="descname">trans_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.trans_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.objectstorage.ContainerObject.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.objectstorage.ContainerObject.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.ContainerObject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.objectstorage.TempUrl">
<em class="property">class </em><code class="descclassname">pulumi_openstack.objectstorage.</code><code class="descname">TempUrl</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>container=None</em>, <em>method=None</em>, <em>object=None</em>, <em>regenerate=None</em>, <em>region=None</em>, <em>split=None</em>, <em>ttl=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to generate an OpenStack Object Storage temporary URL.</p>
<p>The temporary URL will be valid for as long as TTL is set to (in seconds).
Once the URL has expired, it will no longer be valid, but the resource
will remain in place. If you wish to automatically regenerate a URL, set
the <code class="docutils literal notranslate"><span class="pre">regenerate</span></code> argument to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This will create a new resource with
a new ID and URL.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>container</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container name the object belongs to.</li>
<li><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method allowed when accessing this URL.
Valid values are <code class="docutils literal notranslate"><span class="pre">GET</span></code>, and <code class="docutils literal notranslate"><span class="pre">POST</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">GET</span></code>.</li>
<li><strong>object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object name the tempurl is for.</li>
<li><strong>regenerate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically regenerate the URL when
it has expired. If set to true, this will create a new resource with a new
ID and new URL. Defaults to false.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region the tempurl is located in.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The TTL, in seconds, for the URL. For how long it should
be valid.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.TempUrl.container">
<code class="descname">container</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.container" title="Permalink to this definition">¶</a></dt>
<dd><p>The container name the object belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.TempUrl.method">
<code class="descname">method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The method allowed when accessing this URL.
Valid values are <code class="docutils literal notranslate"><span class="pre">GET</span></code>, and <code class="docutils literal notranslate"><span class="pre">POST</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">GET</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.TempUrl.object">
<code class="descname">object</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.object" title="Permalink to this definition">¶</a></dt>
<dd><p>The object name the tempurl is for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.TempUrl.regenerate">
<code class="descname">regenerate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.regenerate" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically regenerate the URL when
it has expired. If set to true, this will create a new resource with a new
ID and new URL. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.TempUrl.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the tempurl is located in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.TempUrl.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL, in seconds, for the URL. For how long it should
be valid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.objectstorage.TempUrl.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.objectstorage.TempUrl.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.objectstorage.TempUrl.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.objectstorage.TempUrl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
