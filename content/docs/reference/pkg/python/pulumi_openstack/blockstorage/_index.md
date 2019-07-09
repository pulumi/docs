---
---

<div class="section" id="blockstorage">
<h1>blockstorage<a class="headerlink" href="#blockstorage" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_openstack.blockstorage"></span><dl class="class">
<dt id="pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result">
<em class="property">class </em><code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">GetAvailabilityZonesV3Result</code><span class="sig-paren">(</span><em>names=None</em>, <em>region=None</em>, <em>state=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAvailabilityZonesV3.</p>
<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result.names">
<code class="descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of the availability zones, ordered alphanumerically, that
match the queried <code class="docutils literal notranslate"><span class="pre">state</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result.state" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetAvailabilityZonesV3Result.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result">
<em class="property">class </em><code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">GetSnapshotV2Result</code><span class="sig-paren">(</span><em>description=None</em>, <em>metadata=None</em>, <em>most_recent=None</em>, <em>name=None</em>, <em>region=None</em>, <em>size=None</em>, <em>status=None</em>, <em>volume_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshotV2.</p>
<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot’s description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot’s metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result.status" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV2Result.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV2Result.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result">
<em class="property">class </em><code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">GetSnapshotV3Result</code><span class="sig-paren">(</span><em>description=None</em>, <em>metadata=None</em>, <em>most_recent=None</em>, <em>name=None</em>, <em>region=None</em>, <em>size=None</em>, <em>status=None</em>, <em>volume_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshotV3.</p>
<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot’s description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot’s metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result.status" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.GetSnapshotV3Result.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.GetSnapshotV3Result.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.blockstorage.Volume">
<em class="property">class </em><code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">Volume</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zone=None</em>, <em>consistency_group_id=None</em>, <em>description=None</em>, <em>enable_online_resize=None</em>, <em>image_id=None</em>, <em>metadata=None</em>, <em>multiattach=None</em>, <em>name=None</em>, <em>region=None</em>, <em>size=None</em>, <em>snapshot_id=None</em>, <em>source_replica=None</em>, <em>source_vol_id=None</em>, <em>volume_type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V3 volume resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The availability zone for the volume.
Changing this creates a new volume.</li>
<li><strong>consistency_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The consistency group to place the volume
in.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the volume. Changing this updates
the volume’s description.</li>
<li><strong>enable_online_resize</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When this option is set it allows extending
attached volumes. Note: updating size of an attached volume requires Cinder
support for version 3.42 and a compatible storage driver.</li>
<li><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.</li>
<li><strong>multiattach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow the volume to be attached to more than one Compute instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the volume. Changing this updates the
volume’s name.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the volume to create (in gigabytes).</li>
<li><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The snapshot ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>source_replica</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The volume ID to replicate with.</li>
<li><strong>source_vol_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The volume ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>volume_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of volume to create.
Changing this creates a new volume.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_v3.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.attachments">
<code class="descname">attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone for the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.consistency_group_id">
<code class="descname">consistency_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.consistency_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The consistency group to place the volume
in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the volume. Changing this updates
the volume’s description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.enable_online_resize">
<code class="descname">enable_online_resize</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.enable_online_resize" title="Permalink to this definition">¶</a></dt>
<dd><p>When this option is set it allows extending
attached volumes. Note: updating size of an attached volume requires Cinder
support for version 3.42 and a compatible storage driver.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The image ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.multiattach">
<code class="descname">multiattach</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.multiattach" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow the volume to be attached to more than one Compute instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the volume. Changing this updates the
volume’s name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the volume to create (in gigabytes).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.source_replica">
<code class="descname">source_replica</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.source_replica" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID to replicate with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.source_vol_id">
<code class="descname">source_vol_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.source_vol_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.Volume.volume_type">
<code class="descname">volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of volume to create.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.blockstorage.Volume.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.Volume.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.VolumeAttach">
<em class="property">class </em><code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">VolumeAttach</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attach_mode=None</em>, <em>device=None</em>, <em>host_name=None</em>, <em>initiator=None</em>, <em>ip_address=None</em>, <em>multipath=None</em>, <em>os_type=None</em>, <em>platform=None</em>, <em>region=None</em>, <em>volume_id=None</em>, <em>wwnn=None</em>, <em>wwpns=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource is experimental and may be removed in the future! Feedback
is requested if you find this resource useful or if you find any problems
with it.</p>
<p>Creates a general purpose attachment connection to a Block
Storage volume using the OpenStack Block Storage (Cinder) v3 API.
Depending on your Block Storage service configuration, this
resource can assist in attaching a volume to a non-OpenStack resource
such as a bare-metal server or a remote virtual machine in a
different cloud provider.</p>
<p>This does not actually attach a volume to an instance. Please use
the <code class="docutils literal notranslate"><span class="pre">openstack_compute_volume_attach_v3</span></code> resource for that.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attach_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify whether to attach the volume as Read-Only
(<code class="docutils literal notranslate"><span class="pre">ro</span></code>) or Read-Write (<code class="docutils literal notranslate"><span class="pre">rw</span></code>). Only values of <code class="docutils literal notranslate"><span class="pre">ro</span></code> and <code class="docutils literal notranslate"><span class="pre">rw</span></code> are accepted.
If left unspecified, the Block Storage API will apply a default of <code class="docutils literal notranslate"><span class="pre">rw</span></code>.</li>
<li><strong>device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify <code class="docutils literal notranslate"><span class="pre">auto</span></code> or a device such as <code class="docutils literal notranslate"><span class="pre">/dev/vdc</span></code>.</li>
<li><strong>host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host to attach the volume to.</li>
<li><strong>initiator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The iSCSI initiator string to make the connection.</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the <code class="docutils literal notranslate"><span class="pre">host_name</span></code> above.</li>
<li><strong>multipath</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to connect to this volume via multipath.</li>
<li><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The iSCSI initiator OS type.</li>
<li><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The iSCSI initiator platform.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume attachment.</li>
<li><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Volume to attach to an Instance.</li>
<li><strong>wwnn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A wwnn name. Used for Fibre Channel connections.</li>
<li><strong>wwpns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of wwpn strings. Used for Fibre Channel
connections.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_attach_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_attach_v3.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.attach_mode">
<code class="descname">attach_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.attach_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify whether to attach the volume as Read-Only
(<code class="docutils literal notranslate"><span class="pre">ro</span></code>) or Read-Write (<code class="docutils literal notranslate"><span class="pre">rw</span></code>). Only values of <code class="docutils literal notranslate"><span class="pre">ro</span></code> and <code class="docutils literal notranslate"><span class="pre">rw</span></code> are accepted.
If left unspecified, the Block Storage API will apply a default of <code class="docutils literal notranslate"><span class="pre">rw</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.data">
<code class="descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.data" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.device">
<code class="descname">device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.device" title="Permalink to this definition">¶</a></dt>
<dd><p>The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify <code class="docutils literal notranslate"><span class="pre">auto</span></code> or a device such as <code class="docutils literal notranslate"><span class="pre">/dev/vdc</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.driver_volume_type">
<code class="descname">driver_volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.driver_volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The storage driver that the volume is based on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.host_name">
<code class="descname">host_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The host to attach the volume to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.initiator">
<code class="descname">initiator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.initiator" title="Permalink to this definition">¶</a></dt>
<dd><p>The iSCSI initiator string to make the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the <code class="docutils literal notranslate"><span class="pre">host_name</span></code> above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.mount_point_base">
<code class="descname">mount_point_base</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.mount_point_base" title="Permalink to this definition">¶</a></dt>
<dd><p>A mount point base name for shared storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.multipath">
<code class="descname">multipath</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.multipath" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to connect to this volume via multipath.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.os_type">
<code class="descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The iSCSI initiator OS type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.platform">
<code class="descname">platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The iSCSI initiator platform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V3 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume attachment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Volume to attach to an Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.wwnn">
<code class="descname">wwnn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.wwnn" title="Permalink to this definition">¶</a></dt>
<dd><p>A wwnn name. Used for Fibre Channel connections.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.wwpns">
<code class="descname">wwpns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.wwpns" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of wwpn strings. Used for Fibre Channel
connections.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.blockstorage.VolumeAttach.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.VolumeAttach.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttach.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2">
<em class="property">class </em><code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">VolumeAttachV2</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attach_mode=None</em>, <em>device=None</em>, <em>host_name=None</em>, <em>initiator=None</em>, <em>ip_address=None</em>, <em>multipath=None</em>, <em>os_type=None</em>, <em>platform=None</em>, <em>region=None</em>, <em>volume_id=None</em>, <em>wwnn=None</em>, <em>wwpns=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource is experimental and may be removed in the future! Feedback
is requested if you find this resource useful or if you find any problems
with it.</p>
<p>Creates a general purpose attachment connection to a Block
Storage volume using the OpenStack Block Storage (Cinder) v2 API.
Depending on your Block Storage service configuration, this
resource can assist in attaching a volume to a non-OpenStack resource
such as a bare-metal server or a remote virtual machine in a
different cloud provider.</p>
<p>This does not actually attach a volume to an instance. Please use
the <code class="docutils literal notranslate"><span class="pre">openstack_compute_volume_attach_v2</span></code> resource for that.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attach_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify whether to attach the volume as Read-Only
(<code class="docutils literal notranslate"><span class="pre">ro</span></code>) or Read-Write (<code class="docutils literal notranslate"><span class="pre">rw</span></code>). Only values of <code class="docutils literal notranslate"><span class="pre">ro</span></code> and <code class="docutils literal notranslate"><span class="pre">rw</span></code> are accepted.
If left unspecified, the Block Storage API will apply a default of <code class="docutils literal notranslate"><span class="pre">rw</span></code>.</li>
<li><strong>device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify <code class="docutils literal notranslate"><span class="pre">auto</span></code> or a device such as <code class="docutils literal notranslate"><span class="pre">/dev/vdc</span></code>.</li>
<li><strong>host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host to attach the volume to.</li>
<li><strong>initiator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The iSCSI initiator string to make the connection.</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the <code class="docutils literal notranslate"><span class="pre">host_name</span></code> above.</li>
<li><strong>multipath</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to connect to this volume via multipath.</li>
<li><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The iSCSI initiator OS type.</li>
<li><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The iSCSI initiator platform.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume attachment.</li>
<li><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Volume to attach to an Instance.</li>
<li><strong>wwnn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A wwnn name. Used for Fibre Channel connections.</li>
<li><strong>wwpns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of wwpn strings. Used for Fibre Channel
connections.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_attach_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_attach_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.attach_mode">
<code class="descname">attach_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.attach_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify whether to attach the volume as Read-Only
(<code class="docutils literal notranslate"><span class="pre">ro</span></code>) or Read-Write (<code class="docutils literal notranslate"><span class="pre">rw</span></code>). Only values of <code class="docutils literal notranslate"><span class="pre">ro</span></code> and <code class="docutils literal notranslate"><span class="pre">rw</span></code> are accepted.
If left unspecified, the Block Storage API will apply a default of <code class="docutils literal notranslate"><span class="pre">rw</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.data">
<code class="descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.data" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.device">
<code class="descname">device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.device" title="Permalink to this definition">¶</a></dt>
<dd><p>The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify <code class="docutils literal notranslate"><span class="pre">auto</span></code> or a device such as <code class="docutils literal notranslate"><span class="pre">/dev/vdc</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.driver_volume_type">
<code class="descname">driver_volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.driver_volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The storage driver that the volume is based on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.host_name">
<code class="descname">host_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The host to attach the volume to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.initiator">
<code class="descname">initiator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.initiator" title="Permalink to this definition">¶</a></dt>
<dd><p>The iSCSI initiator string to make the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the <code class="docutils literal notranslate"><span class="pre">host_name</span></code> above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.mount_point_base">
<code class="descname">mount_point_base</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.mount_point_base" title="Permalink to this definition">¶</a></dt>
<dd><p>A mount point base name for shared storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.multipath">
<code class="descname">multipath</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.multipath" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to connect to this volume via multipath.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.os_type">
<code class="descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The iSCSI initiator OS type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.platform">
<code class="descname">platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The iSCSI initiator platform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume attachment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Volume to attach to an Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.wwnn">
<code class="descname">wwnn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.wwnn" title="Permalink to this definition">¶</a></dt>
<dd><p>A wwnn name. Used for Fibre Channel connections.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.wwpns">
<code class="descname">wwpns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.wwpns" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of wwpn strings. Used for Fibre Channel
connections.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.VolumeAttachV2.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeAttachV2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.VolumeV1">
<em class="property">class </em><code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">VolumeV1</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zone=None</em>, <em>description=None</em>, <em>image_id=None</em>, <em>metadata=None</em>, <em>name=None</em>, <em>region=None</em>, <em>size=None</em>, <em>snapshot_id=None</em>, <em>source_vol_id=None</em>, <em>volume_type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 volume resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The availability zone for the volume.
Changing this creates a new volume.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the volume. Changing this updates
the volume’s description.</li>
<li><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the volume. Changing this updates the
volume’s name.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the volume to create (in gigabytes). Changing
this creates a new volume.</li>
<li><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The snapshot ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>source_vol_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The volume ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>volume_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of volume to create.
Changing this creates a new volume.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_v1.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.attachments">
<code class="descname">attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone for the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the volume. Changing this updates
the volume’s description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The image ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the volume. Changing this updates the
volume’s name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the volume to create (in gigabytes). Changing
this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.source_vol_id">
<code class="descname">source_vol_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.source_vol_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV1.volume_type">
<code class="descname">volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of volume to create.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.blockstorage.VolumeV1.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.VolumeV1.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.VolumeV2">
<em class="property">class </em><code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">VolumeV2</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zone=None</em>, <em>consistency_group_id=None</em>, <em>description=None</em>, <em>image_id=None</em>, <em>metadata=None</em>, <em>name=None</em>, <em>region=None</em>, <em>size=None</em>, <em>snapshot_id=None</em>, <em>source_replica=None</em>, <em>source_vol_id=None</em>, <em>volume_type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 volume resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The availability zone for the volume.
Changing this creates a new volume.</li>
<li><strong>consistency_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The consistency group to place the volume
in.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the volume. Changing this updates
the volume’s description.</li>
<li><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the volume. Changing this updates the
volume’s name.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the volume to create (in gigabytes). Changing
this creates a new volume.</li>
<li><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The snapshot ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>source_replica</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The volume ID to replicate with.</li>
<li><strong>source_vol_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The volume ID from which to create the volume.
Changing this creates a new volume.</li>
<li><strong>volume_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of volume to create.
Changing this creates a new volume.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.attachments">
<code class="descname">attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone for the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.consistency_group_id">
<code class="descname">consistency_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.consistency_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The consistency group to place the volume
in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the volume. Changing this updates
the volume’s description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The image ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the volume. Changing this updates the
volume’s name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the volume to create (in gigabytes). Changing
this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.snapshot_id">
<code class="descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.source_replica">
<code class="descname">source_replica</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.source_replica" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID to replicate with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.source_vol_id">
<code class="descname">source_vol_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.source_vol_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The volume ID from which to create the volume.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.blockstorage.VolumeV2.volume_type">
<code class="descname">volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of volume to create.
Changing this creates a new volume.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.blockstorage.VolumeV2.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.VolumeV2.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.VolumeV2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.blockstorage.get_availability_zones_v3">
<code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">get_availability_zones_v3</code><span class="sig-paren">(</span><em>region=None</em>, <em>state=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.get_availability_zones_v3" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of Block Storage availability zones from OpenStack</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_availability_zones_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_availability_zones_v3.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.blockstorage.get_snapshot_v2">
<code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">get_snapshot_v2</code><span class="sig-paren">(</span><em>most_recent=None</em>, <em>name=None</em>, <em>region=None</em>, <em>status=None</em>, <em>volume_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.get_snapshot_v2" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an existing snapshot.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_snapshot_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_snapshot_v2.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.blockstorage.get_snapshot_v3">
<code class="descclassname">pulumi_openstack.blockstorage.</code><code class="descname">get_snapshot_v3</code><span class="sig-paren">(</span><em>most_recent=None</em>, <em>name=None</em>, <em>region=None</em>, <em>status=None</em>, <em>volume_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.blockstorage.get_snapshot_v3" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an existing snapshot.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_snapshot_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_snapshot_v3.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
