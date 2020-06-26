---
title: Package pulumi_aws
title_tag: Package pulumi_aws | Python SDK
linktitle: pulumi_aws
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "aws" >}}

<div class="section" id="pulumi-aws">
<h1>Pulumi AWS<a class="headerlink" href="#pulumi-aws" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws"></span><dl class="py class">
<dt id="pulumi_aws.AwaitableGetAmiIdsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetAmiIdsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">executable_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_ascending</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetAmiIdsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetAmiResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetAmiResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">architecture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_device_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">executable_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hypervisor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_owner_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kernel_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ramdisk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_device_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_device_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sriov_net_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_reason</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtualization_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetAmiResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetArnResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetArnResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetArnResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetAutoscalingGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetAutoscalingGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetAutoscalingGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetAvailabilityZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetAvailabilityZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_border_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opt_in_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetAvailabilityZoneResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetAvailabilityZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetAvailabilityZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklisted_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklisted_zone_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetAvailabilityZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetBillingServiceAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetBillingServiceAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetBillingServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetCallerIdentityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetCallerIdentityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetCallerIdentityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetCanonicalUserIdResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetCanonicalUserIdResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetCanonicalUserIdResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetElasticIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetElasticIpResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">association_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_owned_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_owned_ipv4_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interface_owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetElasticIpResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sync_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetPartitionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetPartitionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dns_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetPartitionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetPrefixListResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetPrefixListResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix_list_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetPrefixListResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetRegionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetRegionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetRegionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.AwaitableGetRegionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">AwaitableGetRegionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.AwaitableGetRegionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetAmiIdsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetAmiIdsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">executable_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_ascending</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetAmiIdsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAmiIds.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetAmiIdsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiIdsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetAmiResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetAmiResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">architecture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_device_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">executable_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hypervisor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_owner_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kernel_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ramdisk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_device_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_device_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sriov_net_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_reason</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtualization_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetAmiResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAmi.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.architecture">
<code class="sig-name descname">architecture</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>The OS architecture of the AMI (ie: <code class="docutils literal notranslate"><span class="pre">i386</span></code> or <code class="docutils literal notranslate"><span class="pre">x86_64</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AMI.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.block_device_mappings">
<code class="sig-name descname">block_device_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.block_device_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>The block device mappings of the AMI.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.device_name</span></code> - The physical name of the device.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.ebs.delete_on_termination</span></code> - <code class="docutils literal notranslate"><span class="pre">true</span></code> if the EBS volume
will be deleted on termination.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.ebs.encrypted</span></code> - <code class="docutils literal notranslate"><span class="pre">true</span></code> if the EBS volume
is encrypted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.ebs.iops</span></code> - <code class="docutils literal notranslate"><span class="pre">0</span></code> if the EBS volume is
not a provisioned IOPS image, otherwise the supported IOPS count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.ebs.snapshot_id</span></code> - The ID of the snapshot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.ebs.volume_size</span></code> - The size of the volume, in GiB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.ebs.volume_type</span></code> - The volume type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.no_device</span></code> - Suppresses the specified device
included in the block device mapping of the AMI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">block_device_mappings.#.virtual_name</span></code> - The virtual device name (for
instance stores).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.creation_date">
<code class="sig-name descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the image was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the AMI that was provided during image
creation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.hypervisor">
<code class="sig-name descname">hypervisor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.hypervisor" title="Permalink to this definition">¶</a></dt>
<dd><p>The hypervisor type of the image.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AMI. Should be the same as the resource <code class="docutils literal notranslate"><span class="pre">id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.image_location">
<code class="sig-name descname">image_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.image_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the AMI.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.image_owner_alias">
<code class="sig-name descname">image_owner_alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.image_owner_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account alias (for example, <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">self</span></code>) or
the AWS account ID of the AMI owner.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.image_type">
<code class="sig-name descname">image_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.image_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of image.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.kernel_id">
<code class="sig-name descname">kernel_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.kernel_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The kernel associated with the image, if any. Only applicable
for machine images.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the AMI that was provided during image creation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account ID of the image owner.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.platform">
<code class="sig-name descname">platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The value is Windows for <code class="docutils literal notranslate"><span class="pre">Windows</span></code> AMIs; otherwise blank.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.product_codes">
<code class="sig-name descname">product_codes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.product_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>Any product codes associated with the AMI.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">product_codes.#.product_code_id</span></code> - The product code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product_codes.#.product_code_type</span></code> - The type of product code.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.public">
<code class="sig-name descname">public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.public" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">true</span></code> if the image has public launch permissions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.ramdisk_id">
<code class="sig-name descname">ramdisk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.ramdisk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The RAM disk associated with the image, if any. Only applicable
for machine images.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.root_device_name">
<code class="sig-name descname">root_device_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.root_device_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The device name of the root device.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.root_device_type">
<code class="sig-name descname">root_device_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.root_device_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of root device (ie: <code class="docutils literal notranslate"><span class="pre">ebs</span></code> or <code class="docutils literal notranslate"><span class="pre">instance-store</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.root_snapshot_id">
<code class="sig-name descname">root_snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.root_snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot id associated with the root device, if any
(only applies to <code class="docutils literal notranslate"><span class="pre">ebs</span></code> root devices).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.sriov_net_support">
<code class="sig-name descname">sriov_net_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.sriov_net_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether enhanced networking is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the AMI. If the state is <code class="docutils literal notranslate"><span class="pre">available</span></code>, the image
is successfully registered and can be used to launch an instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.state_reason">
<code class="sig-name descname">state_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.state_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes a state change. Fields are <code class="docutils literal notranslate"><span class="pre">UNSET</span></code> if not available.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">state_reason.code</span></code> - The reason code for the state change.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state_reason.message</span></code> - The message for the state change.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Any tags assigned to the image.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tags.#.key</span></code> - The key name of the tag.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags.#.value</span></code> - The value of the tag.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAmiResult.virtualization_type">
<code class="sig-name descname">virtualization_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAmiResult.virtualization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of virtualization of the AMI (ie: <code class="docutils literal notranslate"><span class="pre">hvm</span></code> or
<code class="docutils literal notranslate"><span class="pre">paravirtual</span></code>).</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetArnResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetArnResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetArnResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getArn.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetArnResult.account">
<code class="sig-name descname">account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetArnResult.account" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html">ID</a> of the AWS account that owns the resource, without the hyphens.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetArnResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetArnResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetArnResult.partition">
<code class="sig-name descname">partition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetArnResult.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>The partition that the resource is in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetArnResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetArnResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the resource resides in.
Note that the ARNs for some resources do not require a region, so this component might be omitted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetArnResult.resource">
<code class="sig-name descname">resource</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetArnResult.resource" title="Permalink to this definition">¶</a></dt>
<dd><p>The content of this part of the ARN varies by service.
It often includes an indicator of the type of resource—for example, an IAM user or Amazon RDS database —followed by a slash (/) or a colon (:), followed by the resource name itself.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetArnResult.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetArnResult.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces">service namespace</a> that identifies the AWS product.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetAutoscalingGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetAutoscalingGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetAutoscalingGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAutoscalingGroups.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetAutoscalingGroupsResult.arns">
<code class="sig-name descname">arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAutoscalingGroupsResult.arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Autoscaling Groups Arns in the current region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAutoscalingGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAutoscalingGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAutoscalingGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAutoscalingGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Autoscaling Groups in the current region.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetAvailabilityZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetAvailabilityZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_border_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opt_in_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetAvailabilityZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAvailabilityZone.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZoneResult.group_name">
<code class="sig-name descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZoneResult.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>For Availability Zones, this is the same value as the Region name. For Local Zones, the name of the associated group, for example <code class="docutils literal notranslate"><span class="pre">us-west-2-lax-1</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZoneResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZoneResult.name_suffix">
<code class="sig-name descname">name_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZoneResult.name_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>The part of the AZ name that appears after the region name, uniquely identifying the AZ within its region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZoneResult.network_border_group">
<code class="sig-name descname">network_border_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZoneResult.network_border_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the location from which the address is advertised.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZoneResult.opt_in_status">
<code class="sig-name descname">opt_in_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZoneResult.opt_in_status" title="Permalink to this definition">¶</a></dt>
<dd><p>For Availability Zones, this always has the value of <code class="docutils literal notranslate"><span class="pre">opt-in-not-required</span></code>. For Local Zones, this is the opt in status. The possible values are <code class="docutils literal notranslate"><span class="pre">opted-in</span></code> and <code class="docutils literal notranslate"><span class="pre">not-opted-in</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZoneResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZoneResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the selected availability zone resides. This is always the region selected on the provider, since this data source searches only within that region.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetAvailabilityZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetAvailabilityZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklisted_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklisted_zone_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetAvailabilityZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAvailabilityZones.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZonesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZonesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Availability Zone names available to the account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetAvailabilityZonesResult.zone_ids">
<code class="sig-name descname">zone_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetAvailabilityZonesResult.zone_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Availability Zone IDs available to the account.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetBillingServiceAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetBillingServiceAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetBillingServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBillingServiceAccount.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetBillingServiceAccountResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetBillingServiceAccountResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS billing service account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetBillingServiceAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetBillingServiceAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetCallerIdentityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetCallerIdentityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetCallerIdentityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCallerIdentity.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetCallerIdentityResult.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetCallerIdentityResult.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Account ID number of the account that owns or contains the calling entity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetCallerIdentityResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetCallerIdentityResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS ARN associated with the calling entity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetCallerIdentityResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetCallerIdentityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetCallerIdentityResult.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetCallerIdentityResult.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the calling entity.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetCanonicalUserIdResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetCanonicalUserIdResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetCanonicalUserIdResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCanonicalUserId.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetCanonicalUserIdResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetCanonicalUserIdResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-friendly name linked to the canonical user ID. The bucket owner’s display name. <strong>NOTE:</strong> <a class="reference external" href="https://docs.aws.amazon.com/AmazonS3/latest/API/RESTServiceGET.html">This value</a> is only included in the response in the US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), EU (Ireland), and South America (São Paulo) regions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetCanonicalUserIdResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetCanonicalUserIdResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetElasticIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetElasticIpResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">association_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_owned_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_owned_ipv4_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interface_owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetElasticIpResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getElasticIp.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.association_id">
<code class="sig-name descname">association_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.association_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID representing the association of the address with an instance in a VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.customer_owned_ip">
<code class="sig-name descname">customer_owned_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.customer_owned_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Customer Owned IP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.customer_owned_ipv4_pool">
<code class="sig-name descname">customer_owned_ipv4_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.customer_owned_ipv4_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Customer Owned IP Pool. For more on customer owned IP addressed check out <a class="reference external" href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-networking-components.html#ip-addressing">Customer-owned IP addresses guide</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>If VPC Elastic IP, the allocation identifier. If EC2-Classic Elastic IP, the public IP address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the instance that the address is associated with (if any).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.network_interface_owner_id">
<code class="sig-name descname">network_interface_owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.network_interface_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the network interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.private_dns">
<code class="sig-name descname">private_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.private_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The Private DNS associated with the Elastic IP address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.private_ip">
<code class="sig-name descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP address associated with the Elastic IP address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.public_dns">
<code class="sig-name descname">public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>Public DNS associated with the Elastic IP address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.public_ip">
<code class="sig-name descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Public IP address of Elastic IP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.public_ipv4_pool">
<code class="sig-name descname">public_ipv4_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.public_ipv4_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an address pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetElasticIpResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetElasticIpResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of tags associated with Elastic IP.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sync_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpRanges.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetIpRangesResult.cidr_blocks">
<code class="sig-name descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetIpRangesResult.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of CIDR blocks.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetIpRangesResult.create_date">
<code class="sig-name descname">create_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetIpRangesResult.create_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The publication time of the IP ranges (e.g. <code class="docutils literal notranslate"><span class="pre">2016-08-03-23-46-05</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetIpRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetIpRangesResult.ipv6_cidr_blocks">
<code class="sig-name descname">ipv6_cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetIpRangesResult.ipv6_cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of IPv6 CIDR blocks.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetIpRangesResult.sync_token">
<code class="sig-name descname">sync_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetIpRangesResult.sync_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The publication time of the IP ranges, in Unix epoch time format
(e.g. <code class="docutils literal notranslate"><span class="pre">1470267965</span></code>).</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetPartitionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetPartitionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dns_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetPartitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPartition.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetPartitionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetPartitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetPrefixListResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetPrefixListResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix_list_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetPrefixListResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrefixList.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetPrefixListResult.cidr_blocks">
<code class="sig-name descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetPrefixListResult.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of CIDR blocks for the AWS service associated with the prefix list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetPrefixListResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetPrefixListResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetPrefixListResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetPrefixListResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the selected prefix list.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetRegionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetRegionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetRegionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegion.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetRegionResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetRegionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The region’s description in this format: “Location (Region name)”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetRegionResult.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetRegionResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 endpoint for the selected region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetRegionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetRegionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetRegionResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetRegionResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the selected region.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.GetRegionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">GetRegionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.GetRegionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegions.</p>
<dl class="py attribute">
<dt id="pulumi_aws.GetRegionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetRegionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.GetRegionsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.GetRegionsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of regions that meets the criteria.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_account_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assume_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">forbidden_account_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_force_path_style</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_credentials_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_credentials_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_get_ec2_platforms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_metadata_api_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_region_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_requesting_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the aws package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access key for API operations. You can retrieve this from the ‘Security &amp; Credentials’ section of the AWS console.</p></li>
<li><p><strong>ignore_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with settings to ignore resource tags across all resources.</p></li>
<li><p><strong>insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Explicitly allow the provider to perform “insecure” SSL requests. If omitted,default value is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.</p></li>
<li><p><strong>profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The profile for API operations. If not set, the default profile created with <code class="docutils literal notranslate"><span class="pre">aws</span> <span class="pre">configure</span></code> will be used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc.</p></li>
<li><p><strong>s3_force_path_style</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set this to true to force the request to use path-style addressing, i.e., <a class="reference external" href="http://s3.amazonaws.com/BUCKET/KEY">http://s3.amazonaws.com/BUCKET/KEY</a>. By
default, the S3 client will use virtual hosted bucket addressing when possible (<a class="reference external" href="http://BUCKET.s3.amazonaws.com/KEY">http://BUCKET.s3.amazonaws.com/KEY</a>).
Specific to the Amazon S3 service.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret key for API operations. You can retrieve this from the ‘Security &amp; Credentials’ section of the AWS console.</p></li>
<li><p><strong>shared_credentials_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the shared credentials file. If not set this defaults to ~/.aws/credentials.</p></li>
<li><p><strong>skip_credentials_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS
available/implemented.</p></li>
<li><p><strong>skip_get_ec2_platforms</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Skip getting the supported EC2 platforms. Used by users that don’t have ec2:DescribeAccountAttributes permissions.</p></li>
<li><p><strong>skip_region_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Skip static validation of region name. Used by users of alternative AWS-like APIs or users w/ access to regions that are
not public (yet).</p></li>
<li><p><strong>skip_requesting_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – session token. A session token is only required if you are using temporary security credentials.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>assume_role</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">external_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">session_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>endpoints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessanalyzer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">acm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">acmpca</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amplify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apigateway</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationautoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationinsights</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appmesh</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appstream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">appsync</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">athena</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscalingplans</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">budgets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud9</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudfront</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudhsm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudtrail</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchevents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchlogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codeartifact</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codebuild</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codecommit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codedeploy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">codepipeline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cognitoidentity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cognitoidp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configservice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cur</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataexchange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datapipeline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datasync</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">devicefarm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">directconnect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dlm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">docdb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dynamodb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ec2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ecr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">efs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticbeanstalk</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elastictranscoder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">es</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firehose</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forecast</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fsx</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gamelift</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">glacier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">globalaccelerator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">glue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">greengrass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guardduty</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iam</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imagebuilder</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inspector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iotanalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iotevents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesis_analytics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisanalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisanalyticsv2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisvideo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lakeformation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambda_</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lexmodels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">licensemanager</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lightsail</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">macie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedblockchain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">marketplacecatalog</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mediaconnect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mediaconvert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">medialive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mediapackage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mediastore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mediastoredata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mq</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">neptune</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkmanager</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opsworks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outposts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">personalize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pinpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pricing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">qldb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quicksight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">r53</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ram</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redshift</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourcegroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourcegroupstaggingapi</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route53</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route53domains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route53resolver</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3control</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sagemaker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretsmanager</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityhub</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverlessrepo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicecatalog</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicediscovery</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicequotas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stepfunctions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storagegateway</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">swf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">synthetics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transfer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wafregional</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wafv2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">worklink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workmail</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaces</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xray</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ignore_tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key_prefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="py method">
<dt id="pulumi_aws.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.get_ami">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_ami</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">executable_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_ami" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of a registered AMI for use in other
resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_ami</span><span class="p">(</span><span class="n">executable_users</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;self&quot;</span><span class="p">],</span>
    <span class="n">filters</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;name&quot;</span><span class="p">,</span>
            <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;myami-*&quot;</span><span class="p">],</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;root-device-type&quot;</span><span class="p">,</span>
            <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;ebs&quot;</span><span class="p">],</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;virtualization-type&quot;</span><span class="p">,</span>
            <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;hvm&quot;</span><span class="p">],</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">most_recent</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;^myami-\d</span><span class="si">{3}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="n">owners</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;self&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>executable_users</strong> (<em>list</em>) – Limit search to users with <em>explicit</em> launch permission on
the image. Valid items are the numeric account ID or <code class="docutils literal notranslate"><span class="pre">self</span></code>.</p></li>
<li><p><strong>filters</strong> (<em>list</em>) – One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].</p></li>
<li><p><strong>most_recent</strong> (<em>bool</em>) – If more than one result is returned, use the most
recent AMI.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API. This
filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.</p></li>
<li><p><strong>owners</strong> (<em>list</em>) – List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, <code class="docutils literal notranslate"><span class="pre">self</span></code> (the current account), or an AWS owner alias (e.g. <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>).</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – Any tags assigned to the image.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `tags.#.key` - The key name of the tag.
* `tags.#.value` - The value of the tag.
</pre></div>
</div>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the AMI that was provided during image creation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_ami_ids">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_ami_ids</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">executable_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_ascending</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_ami_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of AMI IDs matching the specified criteria.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">ubuntu</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_ami_ids</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;name&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;ubuntu/images/ubuntu-*-*-amd64-server-*&quot;</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">owners</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;099720109477&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>executable_users</strong> (<em>list</em>) – Limit search to users with <em>explicit</em> launch
permission on  the image. Valid items are the numeric account ID or <code class="docutils literal notranslate"><span class="pre">self</span></code>.</p></li>
<li><p><strong>filters</strong> (<em>list</em>) – One or more name/value pairs to filter off of. There
are several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API.
This filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.</p></li>
<li><p><strong>owners</strong> (<em>list</em>) – List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, <code class="docutils literal notranslate"><span class="pre">self</span></code> (the current account), or an AWS owner alias (e.g. <code class="docutils literal notranslate"><span class="pre">amazon</span></code>, <code class="docutils literal notranslate"><span class="pre">aws-marketplace</span></code>, <code class="docutils literal notranslate"><span class="pre">microsoft</span></code>).</p></li>
<li><p><strong>sort_ascending</strong> (<em>bool</em>) – Used to sort AMIs by creation time.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_arn">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_arn</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Parses an Amazon Resource Name (ARN) into its constituent parts.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">db_instance</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_arn</span><span class="p">(</span><span class="n">arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:rds:eu-west-1:123456789012:db:mysql-db&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>arn</strong> (<em>str</em>) – The ARN to parse.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_autoscaling_groups">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_autoscaling_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_autoscaling_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The Autoscaling Groups data source allows access to the list of AWS
ASGs within a specific region. This will allow you to pass a list of AutoScaling Groups to other resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">groups</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_autoscaling_groups</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[</span>
    <span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;key&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;Team&quot;</span><span class="p">],</span>
    <span class="p">},</span>
    <span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;value&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;Pets&quot;</span><span class="p">],</span>
    <span class="p">},</span>
<span class="p">])</span>
<span class="n">slack_notifications</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">autoscaling</span><span class="o">.</span><span class="n">Notification</span><span class="p">(</span><span class="s2">&quot;slackNotifications&quot;</span><span class="p">,</span>
    <span class="n">group_names</span><span class="o">=</span><span class="n">groups</span><span class="o">.</span><span class="n">names</span><span class="p">,</span>
    <span class="n">notifications</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;autoscaling:EC2_INSTANCE_LAUNCH&quot;</span><span class="p">,</span>
        <span class="s2">&quot;autoscaling:EC2_INSTANCE_TERMINATE&quot;</span><span class="p">,</span>
        <span class="s2">&quot;autoscaling:EC2_INSTANCE_LAUNCH_ERROR&quot;</span><span class="p">,</span>
        <span class="s2">&quot;autoscaling:EC2_INSTANCE_TERMINATE_ERROR&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">topic_arn</span><span class="o">=</span><span class="s2">&quot;TOPIC ARN&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>filters</strong> (<em>list</em>) – A filter used to scope the list e.g. by tags. See <a class="reference external" href="http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_Filter.html">related docs</a>.</p>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the filter. The valid values are: <code class="docutils literal notranslate"><span class="pre">auto-scaling-group</span></code>, <code class="docutils literal notranslate"><span class="pre">key</span></code>, <code class="docutils literal notranslate"><span class="pre">value</span></code>, and <code class="docutils literal notranslate"><span class="pre">propagate-at-launch</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The value of the filter.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_availability_zone">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_availability_zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getAvailabilityZone</span></code> provides details about a specific availability zone (AZ)
in the current region.</p>
<p>This can be used both to validate an availability zone given in a variable
and to split the AZ name into its component parts of an AWS region and an
AZ identifier letter. The latter may be useful e.g. for implementing a
consistent subnet numbering scheme across several regions by mapping both
the region and the subnet letter to network numbers.</p>
<p>This is different from the <code class="docutils literal notranslate"><span class="pre">getAvailabilityZones</span></code> (plural) data source,
which provides a list of the available zones.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>all_availability_zones</strong> (<em>bool</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to include all Availability Zones and Local Zones regardless of your opt in status.</p></li>
<li><p><strong>filters</strong> (<em>list</em>) – Configuration block(s) for filtering. Detailed below.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the filter field. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html">EC2 DescribeAvailabilityZones API Reference</a>.</p></li>
<li><p><strong>state</strong> (<em>str</em>) – A specific availability zone state to require. May be any of <code class="docutils literal notranslate"><span class="pre">&quot;available&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;information&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;impaired&quot;</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The zone ID of the availability zone to select.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the filter field. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html">EC2 DescribeAvailabilityZones API Reference</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of values that are accepted for the given filter field. Results will be selected if any given value matches.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_availability_zones">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_availability_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklisted_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklisted_zone_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zones data source allows access to the list of AWS
Availability Zones which can be accessed by an AWS account within the region
configured in the provider.</p>
<p>This is different from the <code class="docutils literal notranslate"><span class="pre">getAvailabilityZone</span></code> (singular) data source,
which provides some details about a specific availability zone.</p>
<blockquote>
<div><p>When <a class="reference external" href="https://aws.amazon.com/about-aws/global-infrastructure/localzones/">Local Zones</a> are enabled in a region, by default the API and this data source include both Local Zones and Availability Zones. To return only Availability Zones, see the example section below.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">available</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_availability_zones</span><span class="p">(</span><span class="n">state</span><span class="o">=</span><span class="s2">&quot;available&quot;</span><span class="p">)</span>
<span class="n">primary</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Subnet</span><span class="p">(</span><span class="s2">&quot;primary&quot;</span><span class="p">,</span> <span class="n">availability_zone</span><span class="o">=</span><span class="n">available</span><span class="o">.</span><span class="n">names</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="c1"># ...</span>
<span class="n">secondary</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Subnet</span><span class="p">(</span><span class="s2">&quot;secondary&quot;</span><span class="p">,</span> <span class="n">availability_zone</span><span class="o">=</span><span class="n">available</span><span class="o">.</span><span class="n">names</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<span class="c1"># ...</span>
</pre></div>
</div>
<p>All Local Zones (regardless of opt-in status):</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_availability_zones</span><span class="p">(</span><span class="n">all_availability_zones</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;opt-in-status&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;not-opted-in&quot;</span><span class="p">,</span>
            <span class="s2">&quot;opted-in&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<p>Only Availability Zones (no Local Zones):</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_availability_zones</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;opt-in-status&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;opt-in-not-required&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>all_availability_zones</strong> (<em>bool</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to include all Availability Zones and Local Zones regardless of your opt in status.</p></li>
<li><p><strong>blacklisted_names</strong> (<em>list</em>) – List of blacklisted Availability Zone names.</p></li>
<li><p><strong>blacklisted_zone_ids</strong> (<em>list</em>) – List of blacklisted Availability Zone IDs.</p></li>
<li><p><strong>filters</strong> (<em>list</em>) – Configuration block(s) for filtering. Detailed below.</p></li>
<li><p><strong>state</strong> (<em>str</em>) – Allows to filter list of Availability Zones based on their
current state. Can be either <code class="docutils literal notranslate"><span class="pre">&quot;available&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;information&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;impaired&quot;</span></code> or
<code class="docutils literal notranslate"><span class="pre">&quot;unavailable&quot;</span></code>. By default the list includes a complete set of Availability Zones
to which the underlying AWS account has access, regardless of their state.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the filter field. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html">EC2 DescribeAvailabilityZones API Reference</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of values that are accepted for the given filter field. Results will be selected if any given value matches.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_billing_service_account">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_billing_service_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_billing_service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the Account ID of the <a class="reference external" href="http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html#step-2">AWS Billing and Cost Management Service Account</a> for the purpose of whitelisting in S3 bucket policy.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">main</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_billing_service_account</span><span class="p">()</span>
<span class="n">billing_logs</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">s3</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;billingLogs&quot;</span><span class="p">,</span>
    <span class="n">acl</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;&quot;&quot;</span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">  &quot;Id&quot;: &quot;Policy&quot;,</span>
<span class="s2">  &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">  &quot;Statement&quot;: [</span>
<span class="s2">    </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">      &quot;Action&quot;: [</span>
<span class="s2">        &quot;s3:GetBucketAcl&quot;, &quot;s3:GetBucketPolicy&quot;</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Resource&quot;: &quot;arn:aws:s3:::my-billing-tf-test-bucket&quot;,</span>
<span class="s2">      &quot;Principal&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">        &quot;AWS&quot;: [</span>
<span class="s2">          &quot;</span><span class="si">{</span><span class="n">main</span><span class="o">.</span><span class="n">arn</span><span class="si">}</span><span class="s2">&quot;</span>
<span class="s2">        ]</span>
<span class="s2">      </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">    </span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">    </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">      &quot;Action&quot;: [</span>
<span class="s2">        &quot;s3:PutObject&quot;</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Resource&quot;: &quot;arn:aws:s3:::my-billing-tf-test-bucket/*&quot;,</span>
<span class="s2">      &quot;Principal&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">        &quot;AWS&quot;: [</span>
<span class="s2">          &quot;</span><span class="si">{</span><span class="n">main</span><span class="o">.</span><span class="n">arn</span><span class="si">}</span><span class="s2">&quot;</span>
<span class="s2">        ]</span>
<span class="s2">      </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">  ]</span>
<span class="se">&#x7D;&#x7D;</span><span class="s2"></span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_caller_identity">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_caller_identity</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_caller_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the access to the effective Account ID, User ID, and ARN in
which this provider is authorized.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_caller_identity</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;accountId&quot;</span><span class="p">,</span> <span class="n">current</span><span class="o">.</span><span class="n">account_id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;callerArn&quot;</span><span class="p">,</span> <span class="n">current</span><span class="o">.</span><span class="n">arn</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;callerUser&quot;</span><span class="p">,</span> <span class="n">current</span><span class="o">.</span><span class="n">user_id</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_canonical_user_id">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_canonical_user_id</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_canonical_user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Canonical User ID data source allows access to the <a class="reference external" href="http://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html">canonical user ID</a>
for the effective account in which this provider is working.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_canonical_user_id</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;canonicalUserId&quot;</span><span class="p">,</span> <span class="n">current</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_elastic_ip">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_elastic_ip</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_elastic_ip" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ec2.Eip</span></code> provides details about a specific Elastic IP.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">by_allocation_id</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_elastic_ip</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;eipalloc-12345678&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">by_filter</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_elastic_ip</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;tag:Name&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;exampleNameTagValue&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">by_public_ip</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_elastic_ip</span><span class="p">(</span><span class="n">public_ip</span><span class="o">=</span><span class="s2">&quot;1.2.3.4&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">by_tags</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_elastic_ip</span><span class="p">(</span><span class="n">tags</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;Name&quot;</span><span class="p">:</span> <span class="s2">&quot;exampleNameTagValue&quot;</span><span class="p">,</span>
<span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – One or more name/value pairs to use as filters. There are several valid keys, for a full reference, check out the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html">EC2 API Reference</a>.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The allocation id of the specific VPC EIP to retrieve. If a classic EIP is required, do NOT set <code class="docutils literal notranslate"><span class="pre">id</span></code>, only set <code class="docutils literal notranslate"><span class="pre">public_ip</span></code></p></li>
<li><p><strong>public_ip</strong> (<em>str</em>) – The public IP of the specific EIP to retrieve.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags, each pair of which must exactly match a pair on the desired Elastic IP</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_ip_ranges">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the IP ranges of various AWS products and services. For more information about the contents of this data source and required JSON syntax if referencing a custom URL, see the <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html">AWS IP Address Ranges documention</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">european_ec2</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_ip_ranges</span><span class="p">(</span><span class="n">regions</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;eu-west-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;eu-central-1&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">services</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ec2&quot;</span><span class="p">])</span>
<span class="n">from_europe</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="s2">&quot;fromEurope&quot;</span><span class="p">,</span>
    <span class="n">ingress</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;from_port&quot;</span><span class="p">:</span> <span class="s2">&quot;443&quot;</span><span class="p">,</span>
        <span class="s2">&quot;to_port&quot;</span><span class="p">:</span> <span class="s2">&quot;443&quot;</span><span class="p">,</span>
        <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
        <span class="s2">&quot;cidr_blocks&quot;</span><span class="p">:</span> <span class="n">european_ec2</span><span class="o">.</span><span class="n">cidr_blocks</span><span class="p">,</span>
        <span class="s2">&quot;ipv6_cidr_blocks&quot;</span><span class="p">:</span> <span class="n">european_ec2</span><span class="o">.</span><span class="n">ipv6_cidr_blocks</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;CreateDate&quot;</span><span class="p">:</span> <span class="n">european_ec2</span><span class="o">.</span><span class="n">create_date</span><span class="p">,</span>
        <span class="s2">&quot;SyncToken&quot;</span><span class="p">:</span> <span class="n">european_ec2</span><span class="o">.</span><span class="n">sync_token</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>regions</strong> (<em>list</em>) – Filter IP ranges by regions (or include all regions, if
omitted). Valid items are <code class="docutils literal notranslate"><span class="pre">global</span></code> (for <code class="docutils literal notranslate"><span class="pre">cloudfront</span></code>) as well as all AWS regions
(e.g. <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>)</p></li>
<li><p><strong>services</strong> (<em>list</em>) – Filter IP ranges by services. Valid items are <code class="docutils literal notranslate"><span class="pre">amazon</span></code>
(for amazon.com), <code class="docutils literal notranslate"><span class="pre">amazon_connect</span></code>, <code class="docutils literal notranslate"><span class="pre">api_gateway</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud9</span></code>, <code class="docutils literal notranslate"><span class="pre">cloudfront</span></code>,
<code class="docutils literal notranslate"><span class="pre">codebuild</span></code>, <code class="docutils literal notranslate"><span class="pre">dynamodb</span></code>, <code class="docutils literal notranslate"><span class="pre">ec2</span></code>, <code class="docutils literal notranslate"><span class="pre">ec2_instance_connect</span></code>, <code class="docutils literal notranslate"><span class="pre">globalaccelerator</span></code>,
<code class="docutils literal notranslate"><span class="pre">route53</span></code>, <code class="docutils literal notranslate"><span class="pre">route53_healthchecks</span></code>, <code class="docutils literal notranslate"><span class="pre">s3</span></code> and <code class="docutils literal notranslate"><span class="pre">workspaces_gateways</span></code>. See the
[<code class="docutils literal notranslate"><span class="pre">service</span></code> attribute][2] documentation for other possible values.</p></li>
<li><p><strong>url</strong> (<em>str</em>) – <p>Custom URL for source JSON file. Syntax must match <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html">AWS IP Address Ranges documention</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">https://ip-ranges.amazonaws.com/ip-ranges.json</span></code>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_partition">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_partition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to lookup current AWS partition in which this provider is working</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_partition</span><span class="p">()</span>
<span class="n">s3_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">get_policy_document</span><span class="p">(</span><span class="n">statements</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;actions&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;s3:ListBucket&quot;</span><span class="p">],</span>
    <span class="s2">&quot;resources&quot;</span><span class="p">:</span> <span class="p">[</span><span class="sa">f</span><span class="s2">&quot;arn:</span><span class="si">{</span><span class="n">current</span><span class="o">.</span><span class="n">partition</span><span class="si">}</span><span class="s2">:s3:::my-bucket&quot;</span><span class="p">],</span>
    <span class="s2">&quot;sid&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
<span class="p">}])</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_prefix_list">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_prefix_list</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix_list_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_prefix_list" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getPrefixList</span></code> provides details about a specific prefix list (PL)
in the current region.</p>
<p>This can be used both to validate a prefix list given in a variable
and to obtain the CIDR blocks (IP address ranges) for the associated
AWS service. The latter may be useful e.g. for adding network ACL
rules.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">private_s3_vpc_endpoint</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">VpcEndpoint</span><span class="p">(</span><span class="s2">&quot;privateS3VpcEndpoint&quot;</span><span class="p">,</span>
    <span class="n">service_name</span><span class="o">=</span><span class="s2">&quot;com.amazonaws.us-west-2.s3&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">aws_vpc</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">private_s3_prefix_list</span> <span class="o">=</span> <span class="n">private_s3_vpc_endpoint</span><span class="o">.</span><span class="n">prefix_list_id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">prefix_list_id</span><span class="p">:</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_prefix_list</span><span class="p">(</span><span class="n">prefix_list_id</span><span class="o">=</span><span class="n">prefix_list_id</span><span class="p">))</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">NetworkAcl</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span> <span class="n">vpc_id</span><span class="o">=</span><span class="n">aws_vpc</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">private_s3_network_acl_rule</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">NetworkAclRule</span><span class="p">(</span><span class="s2">&quot;privateS3NetworkAclRule&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="n">private_s3_prefix_list</span><span class="o">.</span><span class="n">cidr_blocks</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
    <span class="n">egress</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">from_port</span><span class="o">=</span><span class="mi">443</span><span class="p">,</span>
    <span class="n">network_acl_id</span><span class="o">=</span><span class="n">bar</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
    <span class="n">rule_action</span><span class="o">=</span><span class="s2">&quot;allow&quot;</span><span class="p">,</span>
    <span class="n">rule_number</span><span class="o">=</span><span class="mi">200</span><span class="p">,</span>
    <span class="n">to_port</span><span class="o">=</span><span class="mi">443</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_prefix_list</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;prefix-list-id&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;pl-68a54001&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – Configuration block(s) for filtering. Detailed below.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the filter field. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html">EC2 DescribePrefixLists API Reference</a>.</p></li>
<li><p><strong>prefix_list_id</strong> (<em>str</em>) – The ID of the prefix list to select.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the filter field. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html">EC2 DescribePrefixLists API Reference</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of values that are accepted for the given filter field. Results will be selected if any given value matches.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_region">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_region</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_region" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getRegion</span></code> provides details about a specific AWS region.</p>
<p>As well as validating a given region name this resource can be used to
discover the name of the region configured within the provider. The latter
can be useful in a child module which is inheriting an AWS provider
configuration from its parent module.</p>
<p>The following example shows how the resource might be used to obtain
the name of the AWS region configured on the provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_region</span><span class="p">()</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>endpoint</strong> (<em>str</em>) – The EC2 endpoint of the region to select.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The full name of the region to select.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.get_regions">
<code class="sig-prename descclassname">pulumi_aws.</code><code class="sig-name descname">get_regions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">all_regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.get_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about AWS Regions. Can be used to filter regions i.e. by Opt-In status or only regions enabled for current account. To get details like endpoint and description of each region the data source can be combined with the <code class="docutils literal notranslate"><span class="pre">getRegion</span></code> data source.</p>
<p>Enabled AWS Regions:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_regions</span><span class="p">()</span>
</pre></div>
</div>
<p>All the regions regardless of the availability</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_regions</span><span class="p">(</span><span class="n">all_regions</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<p>To see regions that are filtered by <code class="docutils literal notranslate"><span class="pre">&quot;not-opted-in&quot;</span></code>, the <code class="docutils literal notranslate"><span class="pre">all_regions</span></code> argument needs to be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> or no results will be returned.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">current</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_regions</span><span class="p">(</span><span class="n">all_regions</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;opt-in-status&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;not-opted-in&quot;</span><span class="p">],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>all_regions</strong> (<em>bool</em>) – If true the source will query all regions regardless of availability.</p></li>
<li><p><strong>filters</strong> (<em>list</em>) – Configuration block(s) to use as filters. Detailed below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the filter field. Valid values can be found in the [describe-regions AWS CLI Reference][1].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of values that are accepted for the given filter field. Results will be selected if any given value matches.</p></li>
</ul>
</dd></dl>

</div>
