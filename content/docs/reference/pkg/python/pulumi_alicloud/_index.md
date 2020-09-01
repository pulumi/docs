---
title: Package pulumi_alicloud
title_tag: Package pulumi_alicloud | Python SDK
linktitle: pulumi_alicloud
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="pulumi-alicloud">
<h1>Pulumi Alicloud<a class="headerlink" href="#pulumi-alicloud" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud"></span><dl class="py class">
<dt id="pulumi_alicloud.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.AwaitableGetCallerIdentityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">AwaitableGetCallerIdentityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.AwaitableGetCallerIdentityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.AwaitableGetFileCrc64ChecksumResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">AwaitableGetFileCrc64ChecksumResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">checksum</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filename</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.AwaitableGetFileCrc64ChecksumResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.AwaitableGetRegionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">AwaitableGetRegionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">current</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.AwaitableGetRegionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_resource_creation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="py method">
<dt id="pulumi_alicloud.GetAccountResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_alicloud.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID (e.g. “1239306421830812”). It can be used to construct an ARN.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.GetCallerIdentityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">GetCallerIdentityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.GetCallerIdentityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCallerIdentity.</p>
<dl class="py method">
<dt id="pulumi_alicloud.GetCallerIdentityResult.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_alicloud.GetCallerIdentityResult.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetCallerIdentityResult.arn">
<em class="property">property </em><code class="sig-name descname">arn</code><a class="headerlink" href="#pulumi_alicloud.GetCallerIdentityResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Alibaba Cloud Resource Name (ARN) of the user making the call.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetCallerIdentityResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_alicloud.GetCallerIdentityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetCallerIdentityResult.identity_type">
<em class="property">property </em><code class="sig-name descname">identity_type</code><a class="headerlink" href="#pulumi_alicloud.GetCallerIdentityResult.identity_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the princiapal. RAMUser for users.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.GetFileCrc64ChecksumResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">GetFileCrc64ChecksumResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">checksum</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filename</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.GetFileCrc64ChecksumResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFileCrc64Checksum.</p>
<dl class="py method">
<dt id="pulumi_alicloud.GetFileCrc64ChecksumResult.checksum">
<em class="property">property </em><code class="sig-name descname">checksum</code><a class="headerlink" href="#pulumi_alicloud.GetFileCrc64ChecksumResult.checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>the file checksum of crc64.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetFileCrc64ChecksumResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_alicloud.GetFileCrc64ChecksumResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.GetRegionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">GetRegionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">current</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.GetRegionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegions.</p>
<dl class="py method">
<dt id="pulumi_alicloud.GetRegionsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_alicloud.GetRegionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetRegionsResult.ids">
<em class="property">property </em><code class="sig-name descname">ids</code><a class="headerlink" href="#pulumi_alicloud.GetRegionsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of region IDs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetRegionsResult.regions">
<em class="property">property </em><code class="sig-name descname">regions</code><a class="headerlink" href="#pulumi_alicloud.GetRegionsResult.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_resource_creation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py method">
<dt id="pulumi_alicloud.GetZonesResult.available_resource_creation">
<em class="property">property </em><code class="sig-name descname">available_resource_creation</code><a class="headerlink" href="#pulumi_alicloud.GetZonesResult.available_resource_creation" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of resources that can be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetZonesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_alicloud.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetZonesResult.ids">
<em class="property">property </em><code class="sig-name descname">ids</code><a class="headerlink" href="#pulumi_alicloud.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.GetZonesResult.zones">
<em class="property">property </em><code class="sig-name descname">zones</code><a class="headerlink" href="#pulumi_alicloud.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assume_role</span><span class="p">:</span> <span class="n">Union[ProviderAssumeRoleArgs, Mapping[str, Any], Awaitable[Union[ProviderAssumeRoleArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_source</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_role_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoints</span><span class="p">:</span> <span class="n">Union[List[Union[ProviderEndpointArgs, Mapping[str, Any], Awaitable[Union[ProviderEndpointArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ProviderEndpointArgs, Mapping[str, Any], Awaitable[Union[ProviderEndpointArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fc</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_endpoint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mns_endpoint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ots_instance_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_credentials_file</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_region_validation</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the alicloud package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access key for API operations. You can retrieve this from the ‘Security Management’ section of the Alibaba Cloud
console.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID for some service API operations. You can retrieve this from the ‘Security Settings’ section of the
Alibaba Cloud console.</p></li>
<li><p><strong>configuration_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use this to mark a terraform configuration file source.</p></li>
<li><p><strong>ecs_role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RAM Role Name attached on a ECS instance for API operations. You can retrieve this from the ‘Access Control’ section
of the Alibaba Cloud console.</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The profile for API operations. If not set, the default profile created with <code class="docutils literal notranslate"><span class="pre">aliyun</span> <span class="pre">configure</span></code> will be used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where Alibaba Cloud operations will take place. Examples are cn-beijing, cn-hangzhou, eu-central-1, etc.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret key for API operations. You can retrieve this from the ‘Security Management’ section of the Alibaba Cloud
console.</p></li>
<li><p><strong>security_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – security token. A security token is only required if you are using Security Token Service.</p></li>
<li><p><strong>shared_credentials_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the shared credentials file. If not set this defaults to ~/.aliyun/config.json</p></li>
<li><p><strong>skip_region_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Skip static validation of region ID. Used by users of alternative AlibabaCloud-like APIs or users w/ access to regions
that are not public (yet).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_alicloud.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_alicloud.get_account">
<code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_alicloud.get_account.AwaitableGetAccountResult<a class="headerlink" href="#pulumi_alicloud.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides information about the current account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_account</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;currentAccountId&quot;</span><span class="p">,</span> <span class="n">current</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.get_caller_identity">
<code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">get_caller_identity</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_alicloud.get_caller_identity.AwaitableGetCallerIdentityResult<a class="headerlink" href="#pulumi_alicloud.get_caller_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the identity of the current user.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.65.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_caller_identity</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;currentUserArn&quot;</span><span class="p">,</span> <span class="n">current</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.get_file_crc64_checksum">
<code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">get_file_crc64_checksum</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filename</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_alicloud.get_file_crc64_checksum.AwaitableGetFileCrc64ChecksumResult<a class="headerlink" href="#pulumi_alicloud.get_file_crc64_checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source compute file crc64 checksum.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.59.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_file_crc64_checksum</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;exampleFileName&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;fileCrc64Checksum&quot;</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;alicloud_file_crc64_checksum&quot;</span><span class="p">][</span><span class="s2">&quot;defualt&quot;</span><span class="p">][</span><span class="s2">&quot;checksum&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>filename</strong> (<em>str</em>) – The name of the file to be computed crc64 checksum.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.get_regions">
<code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">get_regions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">current</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_alicloud.get_regions.AwaitableGetRegionsResult<a class="headerlink" href="#pulumi_alicloud.get_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides Alibaba Cloud regions.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">current_region_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_regions</span><span class="p">(</span><span class="n">current</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;currentRegionId&quot;</span><span class="p">,</span> <span class="n">current_region_ds</span><span class="o">.</span><span class="n">regions</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>current</strong> (<em>bool</em>) – Set to true to match only the region configured in the provider.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the region to select, such as <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_disk_category</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_instance_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_resource_creation</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_ip_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_alicloud.get_zones.AwaitableGetZonesResult<a class="headerlink" href="#pulumi_alicloud.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If one zone is sold out, it will not be exported.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">zones_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">available_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_ssd&quot;</span><span class="p">,</span>
    <span class="n">available_instance_type</span><span class="o">=</span><span class="s2">&quot;ecs.n4.large&quot;</span><span class="p">)</span>
<span class="c1"># Create an ECS instance with the first matched zone</span>
<span class="n">instance</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;instance&quot;</span><span class="p">,</span> <span class="n">availability_zone</span><span class="o">=</span><span class="n">zones_ds</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>available_disk_category</strong> (<em>str</em>) – Filter the results by a specific disk category. Can be either <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code>.</p></li>
<li><p><strong>available_instance_type</strong> (<em>str</em>) – Filter the results by a specific instance type.</p></li>
<li><p><strong>available_resource_creation</strong> (<em>str</em>) – Filter the results by a specific resource type.
Valid values: <code class="docutils literal notranslate"><span class="pre">Instance</span></code>, <code class="docutils literal notranslate"><span class="pre">Disk</span></code>, <code class="docutils literal notranslate"><span class="pre">VSwitch</span></code>, <code class="docutils literal notranslate"><span class="pre">Rds</span></code>, <code class="docutils literal notranslate"><span class="pre">KVStore</span></code>, <code class="docutils literal notranslate"><span class="pre">FunctionCompute</span></code>, <code class="docutils literal notranslate"><span class="pre">Elasticsearch</span></code>, <code class="docutils literal notranslate"><span class="pre">Slb</span></code>.</p></li>
<li><p><strong>available_slb_address_ip_version</strong> (<em>str</em>) – Filter the results by a slb instance address version. Can be either <code class="docutils literal notranslate"><span class="pre">ipv4</span></code>, or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>&gt; **NOTE:** The disk category `cloud` has been outdated and can only be used by non-I/O Optimized ECS instances. Many availability zones don&#39;t support it. It is recommended to use `cloud_efficiency` or `cloud_ssd`.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>available_slb_address_type</strong> (<em>str</em>) – Filter the results by a slb instance address type. Can be either <code class="docutils literal notranslate"><span class="pre">Vpc</span></code>, <code class="docutils literal notranslate"><span class="pre">classic_internet</span></code> or <code class="docutils literal notranslate"><span class="pre">classic_intranet</span></code></p></li>
<li><p><strong>enable_details</strong> (<em>bool</em>) – Default to false and only output <code class="docutils literal notranslate"><span class="pre">id</span></code> in the <code class="docutils literal notranslate"><span class="pre">zones</span></code> block. Set it to true can output more details.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by a specific ECS instance charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>multi</strong> (<em>bool</em>) – Indicate whether the zones can be used in a multi AZ configuration. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Multi AZ is usually used to launch RDS instances.</p></li>
<li><p><strong>network_type</strong> (<em>str</em>) – Filter the results by a specific network type. Valid values: <code class="docutils literal notranslate"><span class="pre">Classic</span></code> and <code class="docutils literal notranslate"><span class="pre">Vpc</span></code>.</p></li>
<li><p><strong>spot_strategy</strong> (<em>str</em>) – <ul>
<li><p>(Optional) Filter the results by a specific ECS spot type. Valid values: <code class="docutils literal notranslate"><span class="pre">NoSpot</span></code>, <code class="docutils literal notranslate"><span class="pre">SpotWithPriceLimit</span></code> and <code class="docutils literal notranslate"><span class="pre">SpotAsPriceGo</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">NoSpot</span></code>.</p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
