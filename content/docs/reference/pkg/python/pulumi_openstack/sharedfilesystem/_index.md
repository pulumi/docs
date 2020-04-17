---
title: Module sharedfilesystem
title_tag: Module sharedfilesystem | Package pulumi_openstack | Python SDK
linktitle: sharedfilesystem
notitle: true
---

<div class="section" id="sharedfilesystem">
<h1>sharedfilesystem<a class="headerlink" href="#sharedfilesystem" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.sharedfilesystem"></span><dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.AwaitableGetAvailbilityZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">AwaitableGetAvailbilityZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.AwaitableGetAvailbilityZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.AwaitableGetShareNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">AwaitableGetShareNetworkResult</code><span class="sig-paren">(</span><em class="sig-param">cidr=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_type=None</em>, <em class="sig-param">neutron_net_id=None</em>, <em class="sig-param">neutron_subnet_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_service_id=None</em>, <em class="sig-param">security_service_ids=None</em>, <em class="sig-param">segmentation_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.AwaitableGetShareNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.AwaitableGetShareResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">AwaitableGetShareResult</code><span class="sig-paren">(</span><em class="sig-param">availability_zone=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">export_location_path=None</em>, <em class="sig-param">export_locations=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_network_id=None</em>, <em class="sig-param">share_proto=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.AwaitableGetShareResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.AwaitableGetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">AwaitableGetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_id=None</em>, <em class="sig-param">share_proto=None</em>, <em class="sig-param">share_size=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.AwaitableGetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.GetAvailbilityZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">GetAvailbilityZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetAvailbilityZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAvailbilityZones.</p>
<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetAvailbilityZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetAvailbilityZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetAvailbilityZonesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetAvailbilityZonesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of the availability zones, ordered alphanumerically.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetAvailbilityZonesResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetAvailbilityZonesResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">GetShareNetworkResult</code><span class="sig-paren">(</span><em class="sig-param">cidr=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_type=None</em>, <em class="sig-param">neutron_net_id=None</em>, <em class="sig-param">neutron_subnet_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_service_id=None</em>, <em class="sig-param">security_service_ids=None</em>, <em class="sig-param">segmentation_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getShareNetwork.</p>
<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.cidr">
<code class="sig-name descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.ip_version">
<code class="sig-name descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.network_type">
<code class="sig-name descname">network_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.network_type" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.neutron_net_id">
<code class="sig-name descname">neutron_net_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.neutron_net_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.neutron_subnet_id">
<code class="sig-name descname">neutron_subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.neutron_subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the Share Network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.security_service_id">
<code class="sig-name descname">security_service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.security_service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.security_service_ids">
<code class="sig-name descname">security_service_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.security_service_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of security service IDs associated with
the share network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareNetworkResult.segmentation_id">
<code class="sig-name descname">segmentation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareNetworkResult.segmentation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">GetShareResult</code><span class="sig-paren">(</span><em class="sig-param">availability_zone=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">export_location_path=None</em>, <em class="sig-param">export_locations=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_network_id=None</em>, <em class="sig-param">share_proto=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getShare.</p>
<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The share availability zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.export_location_path">
<code class="sig-name descname">export_location_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.export_location_path" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.export_locations">
<code class="sig-name descname">export_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.export_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of export locations. For example, when a share
server has more than one network interface, it can have multiple export
locations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.is_public">
<code class="sig-name descname">is_public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Shared File System client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.share_network_id">
<code class="sig-name descname">share_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.share_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.share_proto">
<code class="sig-name descname">share_proto</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.share_proto" title="Permalink to this definition">¶</a></dt>
<dd><p>The share protocol.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The share size, in GBs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetShareResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetShareResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">GetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_id=None</em>, <em class="sig-param">share_proto=None</em>, <em class="sig-param">share_size=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.share_id">
<code class="sig-name descname">share_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.share_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the source share that was used to create the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.share_proto">
<code class="sig-name descname">share_proto</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.share_proto" title="Permalink to this definition">¶</a></dt>
<dd><p>The file system protocol of a share snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.share_size">
<code class="sig-name descname">share_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.share_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The share snapshot size, in GBs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot size, in GBs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.GetSnapshotResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.GetSnapshotResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">SecurityService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_ip=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ou=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">server=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to configure a security service.</p>
<p>A security service stores configuration information for clients for
authentication and authorization (AuthN/AuthZ). For example, a share server
will be the client for an existing service such as LDAP, Kerberos, or
Microsoft Active Directory.</p>
<p>Minimum supported Manila microversion is 2.7.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the security service.
Changing this updates the description of the existing security service.</p></li>
<li><p><strong>dns_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service DNS IP address that is used inside the
tenant network.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service domain.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security service. Changing this updates the name
of the existing security service.</p></li>
<li><p><strong>ou</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service ou. An organizational unit can be added to
specify where the share ends up. New in Manila microversion 2.44.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user password, if you specify a user.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a security service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security service.</p></li>
<li><p><strong>server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service host name or IP address.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service type - can either be active_directory,
kerberos or ldap.  Changing this updates the existing security service.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service user or group name that is used by the
tenant.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the security service.
Changing this updates the description of the existing security service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.dns_ip">
<code class="sig-name descname">dns_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.dns_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The security service DNS IP address that is used inside the
tenant network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The security service domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security service. Changing this updates the name
of the existing security service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.ou">
<code class="sig-name descname">ou</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.ou" title="Permalink to this definition">¶</a></dt>
<dd><p>The security service ou. An organizational unit can be added to
specify where the share ends up. New in Manila microversion 2.44.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The user password, if you specify a user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the Security Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a security service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.server">
<code class="sig-name descname">server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.server" title="Permalink to this definition">¶</a></dt>
<dd><p>The security service host name or IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The security service type - can either be active_directory,
kerberos or ldap.  Changing this updates the existing security service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The security service user or group name that is used by the
tenant.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_ip=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ou=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">server=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the security service.
Changing this updates the description of the existing security service.</p></li>
<li><p><strong>dns_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service DNS IP address that is used inside the
tenant network.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service domain.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security service. Changing this updates the name
of the existing security service.</p></li>
<li><p><strong>ou</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service ou. An organizational unit can be added to
specify where the share ends up. New in Manila microversion 2.44.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user password, if you specify a user.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Security Service.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a security service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security service.</p></li>
<li><p><strong>server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service host name or IP address.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service type - can either be active_directory,
kerberos or ldap.  Changing this updates the existing security service.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security service user or group name that is used by the
tenant.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.sharedfilesystem.SecurityService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.SecurityService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.sharedfilesystem.Share">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">Share</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_network_id=None</em>, <em class="sig-param">share_proto=None</em>, <em class="sig-param">share_type=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to configure a share.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share availability zone. Changing this creates a
new share.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the share.
Changing this updates the description of the existing share.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more metadata key and value pairs as a dictionary of
strings.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the share. Changing this updates the name
of the existing share.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.</p></li>
<li><p><strong>share_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of a share network where the share server exists
or will be created. If <code class="docutils literal notranslate"><span class="pre">share_network_id</span></code> is not set and you provide a <code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code>,
the share_network_id value from the snapshot is used. Changing this creates a new share.</p></li>
<li><p><strong>share_proto</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.</p></li>
<li><p><strong>share_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share type name. If you omit this parameter, the default
share type is used.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the share’s base snapshot. Changing this creates
a new share.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.all_metadata">
<code class="sig-name descname">all_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.all_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The map of metadata, assigned on the share, which has been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The share availability zone. Changing this creates a
new share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the share.
Changing this updates the description of the existing share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.export_locations">
<code class="sig-name descname">export_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.export_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preferred</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.has_replicas">
<code class="sig-name descname">has_replicas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.has_replicas" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether a share has replicas or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.host">
<code class="sig-name descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The share host name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.is_public">
<code class="sig-name descname">is_public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more metadata key and value pairs as a dictionary of
strings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the share. Changing this updates the name
of the existing share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.replication_type">
<code class="sig-name descname">replication_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.replication_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The share replication type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.share_network_id">
<code class="sig-name descname">share_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.share_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of a share network where the share server exists
or will be created. If <code class="docutils literal notranslate"><span class="pre">share_network_id</span></code> is not set and you provide a <code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code>,
the share_network_id value from the snapshot is used. Changing this creates a new share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.share_proto">
<code class="sig-name descname">share_proto</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.share_proto" title="Permalink to this definition">¶</a></dt>
<dd><p>The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.share_server_id">
<code class="sig-name descname">share_server_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.share_server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the share server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.share_type">
<code class="sig-name descname">share_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.share_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The share type name. If you omit this parameter, the default
share type is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.Share.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the share’s base snapshot. Changing this creates
a new share.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.sharedfilesystem.Share.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">all_metadata=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">export_locations=None</em>, <em class="sig-param">has_replicas=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replication_type=None</em>, <em class="sig-param">share_network_id=None</em>, <em class="sig-param">share_proto=None</em>, <em class="sig-param">share_server_id=None</em>, <em class="sig-param">share_type=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Share resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>all_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The map of metadata, assigned on the share, which has been
explicitly and implicitly added.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share availability zone. Changing this creates a
new share.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the share.
Changing this updates the description of the existing share.</p></li>
<li><p><strong>export_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of export locations. For example, when a share server
has more than one network interface, it can have multiple export locations.</p></li>
<li><p><strong>has_replicas</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether a share has replicas or not.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share host name.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The level of visibility for the share. Set to true to make
share public. Set to false to make it private. Default value is false. Changing this
updates the existing share.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more metadata key and value pairs as a dictionary of
strings.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the share. Changing this updates the name
of the existing share.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Share.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share. Changing this
creates a new share.</p></li>
<li><p><strong>replication_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share replication type.</p></li>
<li><p><strong>share_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of a share network where the share server exists
or will be created. If <code class="docutils literal notranslate"><span class="pre">share_network_id</span></code> is not set and you provide a <code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code>,
the share_network_id value from the snapshot is used. Changing this creates a new share.</p></li>
<li><p><strong>share_proto</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share protocol - can either be NFS, CIFS,
CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.</p></li>
<li><p><strong>share_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the share server.</p></li>
<li><p><strong>share_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share type name. If you omit this parameter, the default
share type is used.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The share size, in GBs. The requested share size cannot be greater
than the allowed GB quota. Changing this resizes the existing share.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the share’s base snapshot. Changing this creates
a new share.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>export_locations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preferred</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.sharedfilesystem.Share.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.sharedfilesystem.Share.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.Share.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">ShareAccess</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_level=None</em>, <em class="sig-param">access_to=None</em>, <em class="sig-param">access_type=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ShareAccess resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] access_level: The access level to the share. Can either be <code class="docutils literal notranslate"><span class="pre">rw</span></code> or <code class="docutils literal notranslate"><span class="pre">ro</span></code>.
:param pulumi.Input[str] access_to: The value that defines the access. Can either be an IP</p>
<blockquote>
<div><p>address or a username verified by configured Security Service of the Share Network.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access rule type. Can either be an ip, user,
cert, or cephx. cephx support requires an OpenStack environment that supports
Shared Filesystem microversion 2.13 (Mitaka) or later.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share access. Changing this
creates a new share access.</p></li>
<li><p><strong>share_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the share to which you are granted access.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.access_key">
<code class="sig-name descname">access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The access credential of the entity granted access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.access_level">
<code class="sig-name descname">access_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The access level to the share. Can either be <code class="docutils literal notranslate"><span class="pre">rw</span></code> or <code class="docutils literal notranslate"><span class="pre">ro</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.access_to">
<code class="sig-name descname">access_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.access_to" title="Permalink to this definition">¶</a></dt>
<dd><p>The value that defines the access. Can either be an IP
address or a username verified by configured Security Service of the Share Network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.access_type">
<code class="sig-name descname">access_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.access_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The access rule type. Can either be an ip, user,
cert, or cephx. cephx support requires an OpenStack environment that supports
Shared Filesystem microversion 2.13 (Mitaka) or later.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share access. Changing this
creates a new share access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.share_id">
<code class="sig-name descname">share_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.share_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the share to which you are granted access.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">access_level=None</em>, <em class="sig-param">access_to=None</em>, <em class="sig-param">access_type=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ShareAccess resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access credential of the entity granted access.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access level to the share. Can either be <code class="docutils literal notranslate"><span class="pre">rw</span></code> or <code class="docutils literal notranslate"><span class="pre">ro</span></code>.</p></li>
<li><p><strong>access_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value that defines the access. Can either be an IP
address or a username verified by configured Security Service of the Share Network.</p></li>
<li><p><strong>access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access rule type. Can either be an ip, user,
cert, or cephx. cephx support requires an OpenStack environment that supports
Shared Filesystem microversion 2.13 (Mitaka) or later.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share access. Changing this
creates a new share access.</p></li>
<li><p><strong>share_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the share to which you are granted access.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.sharedfilesystem.ShareAccess.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareAccess.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">ShareNetwork</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">neutron_net_id=None</em>, <em class="sig-param">neutron_subnet_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_service_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to configure a share network.</p>
<p>A share network stores network information that share servers can use when
shares are created.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the share network.
Changing this updates the description of the existing share network.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the share network. Changing this updates the name
of the existing share network.</p></li>
<li><p><strong>neutron_net_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of a neutron network when setting up or updating
a share network. Changing this updates the existing share network if it’s not used by
shares.</p></li>
<li><p><strong>neutron_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the neutron subnet when setting up or
updating a share network. Changing this updates the existing share network if it’s
not used by shares.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
share network.</p></li>
<li><p><strong>security_service_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of security service IDs to associate with
the share network. The security service must be specified by ID and not name.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.cidr">
<code class="sig-name descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The share network CIDR.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the share network.
Changing this updates the description of the existing share network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.ip_version">
<code class="sig-name descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP version of the share network. Can either be 4 or 6.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the share network. Changing this updates the name
of the existing share network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.network_type">
<code class="sig-name descname">network_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.network_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The share network type. Can either be VLAN, VXLAN, GRE, or flat.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.neutron_net_id">
<code class="sig-name descname">neutron_net_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.neutron_net_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of a neutron network when setting up or updating
a share network. Changing this updates the existing share network if it’s not used by
shares.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.neutron_subnet_id">
<code class="sig-name descname">neutron_subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.neutron_subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the neutron subnet when setting up or
updating a share network. Changing this updates the existing share network if it’s
not used by shares.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the Share Network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
share network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.security_service_ids">
<code class="sig-name descname">security_service_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.security_service_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of security service IDs to associate with
the share network. The security service must be specified by ID and not name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.segmentation_id">
<code class="sig-name descname">segmentation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.segmentation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The share network segmentation ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_type=None</em>, <em class="sig-param">neutron_net_id=None</em>, <em class="sig-param">neutron_subnet_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_service_ids=None</em>, <em class="sig-param">segmentation_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ShareNetwork resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share network CIDR.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the share network.
Changing this updates the description of the existing share network.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The IP version of the share network. Can either be 4 or 6.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the share network. Changing this updates the name
of the existing share network.</p></li>
<li><p><strong>network_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The share network type. Can either be VLAN, VXLAN, GRE, or flat.</p></li>
<li><p><strong>neutron_net_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of a neutron network when setting up or updating
a share network. Changing this updates the existing share network if it’s not used by
shares.</p></li>
<li><p><strong>neutron_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the neutron subnet when setting up or
updating a share network. Changing this updates the existing share network if it’s
not used by shares.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Share Network.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to create a share network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
share network.</p></li>
<li><p><strong>security_service_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of security service IDs to associate with
the share network. The security service must be specified by ID and not name.</p></li>
<li><p><strong>segmentation_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The share network segmentation ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.sharedfilesystem.ShareNetwork.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.ShareNetwork.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.sharedfilesystem.get_availbility_zones">
<code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">get_availbility_zones</code><span class="sig-paren">(</span><em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.get_availbility_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of Shared File System availability zones
from OpenStack</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Shared File System
client. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.sharedfilesystem.get_share">
<code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">get_share</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">export_location_path=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_network_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.get_share" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available Shared File System share.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – The human-readable description for the share.</p></li>
<li><p><strong>export_location_path</strong> (<em>str</em>) – The export location path of the share. Available
since Manila API version 2.35.</p></li>
<li><p><strong>is_public</strong> (<em>bool</em>) – The level of visibility for the share.
length.</p></li>
<li><p><strong>metadata</strong> (<em>dict</em>) – One or more metadata key and value pairs as a dictionary of
strings.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the share.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Shared File System client.</p></li>
<li><p><strong>share_network_id</strong> (<em>str</em>) – The UUID of the share’s share network.</p></li>
<li><p><strong>snapshot_id</strong> (<em>str</em>) – The UUID of the share’s base snapshot.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – A share status filter. A valid value is <code class="docutils literal notranslate"><span class="pre">creating</span></code>,
<code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">available</span></code>, <code class="docutils literal notranslate"><span class="pre">deleting</span></code>, <code class="docutils literal notranslate"><span class="pre">error_deleting</span></code>, <code class="docutils literal notranslate"><span class="pre">manage_starting</span></code>,
<code class="docutils literal notranslate"><span class="pre">manage_error</span></code>, <code class="docutils literal notranslate"><span class="pre">unmanage_starting</span></code>, <code class="docutils literal notranslate"><span class="pre">unmanage_error</span></code>, <code class="docutils literal notranslate"><span class="pre">unmanaged</span></code>,
<code class="docutils literal notranslate"><span class="pre">extending</span></code>, <code class="docutils literal notranslate"><span class="pre">extending_error</span></code>, <code class="docutils literal notranslate"><span class="pre">shrinking</span></code>, <code class="docutils literal notranslate"><span class="pre">shrinking_error</span></code>, or
<code class="docutils literal notranslate"><span class="pre">shrinking_possible_data_loss_error</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.sharedfilesystem.get_share_network">
<code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">get_share_network</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_type=None</em>, <em class="sig-param">neutron_net_id=None</em>, <em class="sig-param">neutron_subnet_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_service_id=None</em>, <em class="sig-param">segmentation_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.get_share_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available Shared File System share network.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – The human-readable description of the share network.</p></li>
<li><p><strong>ip_version</strong> (<em>float</em>) – The IP version of the share network. Can either be 4 or 6.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the share network.</p></li>
<li><p><strong>network_type</strong> (<em>str</em>) – The share network type. Can either be VLAN, VXLAN,
GRE, or flat.</p></li>
<li><p><strong>neutron_net_id</strong> (<em>str</em>) – The neutron network UUID of the share network.</p></li>
<li><p><strong>neutron_subnet_id</strong> (<em>str</em>) – The neutron subnet UUID of the share network.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Shared File System client.
A Shared File System client is needed to read a share network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>security_service_id</strong> (<em>str</em>) – The security service IDs associated with
the share network.</p></li>
<li><p><strong>segmentation_id</strong> (<em>float</em>) – The share network segmentation ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.sharedfilesystem.get_snapshot">
<code class="sig-prename descclassname">pulumi_openstack.sharedfilesystem.</code><code class="sig-name descname">get_snapshot</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">share_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.sharedfilesystem.get_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available Shared File System snapshot.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – The human-readable description of the snapshot.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the snapshot.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Shared File System client.</p></li>
<li><p><strong>share_id</strong> (<em>str</em>) – The UUID of the source share that was used to create the snapshot.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – A snapshot status filter. A valid value is <code class="docutils literal notranslate"><span class="pre">available</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>,
<code class="docutils literal notranslate"><span class="pre">creating</span></code>, <code class="docutils literal notranslate"><span class="pre">deleting</span></code>, <code class="docutils literal notranslate"><span class="pre">manage_starting</span></code>, <code class="docutils literal notranslate"><span class="pre">manage_error</span></code>, <code class="docutils literal notranslate"><span class="pre">unmanage_starting</span></code>,
<code class="docutils literal notranslate"><span class="pre">unmanage_error</span></code> or <code class="docutils literal notranslate"><span class="pre">error_deleting</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
