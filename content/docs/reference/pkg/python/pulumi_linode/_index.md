---
title: Package pulumi_linode
title_tag: Package pulumi_linode | Python SDK
linktitle: pulumi_linode
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "linode" >}}

<div class="section" id="pulumi-linode">
<h1>Pulumi Linode<a class="headerlink" href="#pulumi-linode" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-linode/issues">pulumi/pulumi-linode repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/issues">terraform-providers/terraform-provider-linode repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_linode"></span><dl class="py class">
<dt id="pulumi_linode.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address1</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zip</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetDomainRecordResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetDomainRecordResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetDomainRecordResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetDomainResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetDomainResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">axfr_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expire_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">soa_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetDomainResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vendor</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetInstanceTypeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetInstanceTypeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">class_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_out</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transfer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vcpus</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetInstanceTypeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetNetworkingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetNetworkingIpResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rdns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_mask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetNetworkingIpResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetObjectStorageClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetObjectStorageClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_site_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetObjectStorageClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetProfileResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorized_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lish_auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">referrals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restricted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">two_factor_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetProfileResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetRegionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetRegionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetRegionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetStackScriptResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetStackScriptResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployments_active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployments_total</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rev_note</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_gravatar_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetStackScriptResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restricted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.AwaitableGetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filesystem_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_linode.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axfr_ips</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expire_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ips</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">soa_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Domain resource.  This can be used to create, modify, and delete Linode Domains through Linode’s managed DNS service.
For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/manager/dns-manager/">DNS Manager</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createDomain">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure a Domain Record attached to a Linode Domain.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foobar_domain</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Domain</span><span class="p">(</span><span class="s2">&quot;foobarDomain&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;foobar.example&quot;</span><span class="p">,</span>
    <span class="n">soa_email</span><span class="o">=</span><span class="s2">&quot;example@foobar.example&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;master&quot;</span><span class="p">)</span>
<span class="n">foobar_domain_record</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">DomainRecord</span><span class="p">(</span><span class="s2">&quot;foobarDomainRecord&quot;</span><span class="p">,</span>
    <span class="n">domain_id</span><span class="o">=</span><span class="n">foobar_domain</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;www&quot;</span><span class="p">,</span>
    <span class="n">record_type</span><span class="o">=</span><span class="s2">&quot;CNAME&quot;</span><span class="p">,</span>
    <span class="n">target</span><span class="o">=</span><span class="s2">&quot;foobar.example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports no additional attributes, however <code class="docutils literal notranslate"><span class="pre">status</span></code> may reflect degraded states.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>axfr_ips</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Domain. This is for display purposes only.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.</p></li>
<li><p><strong>expire_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group this Domain belongs to. This is for display purposes only.</p></li>
<li><p><strong>master_ips</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The IP addresses representing the master DNS for this Domain.</p></li>
<li><p><strong>refresh_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>retry_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>soa_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Start of Authority email address. This is required for master Domains.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to control whether this Domain is currently being rendered (defaults to “active”).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
<li><p><strong>ttl_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axfr_ips</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expire_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ips</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">soa_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.domain.Domain<a class="headerlink" href="#pulumi_linode.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>axfr_ips</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Domain. This is for display purposes only.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.</p></li>
<li><p><strong>expire_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group this Domain belongs to. This is for display purposes only.</p></li>
<li><p><strong>master_ips</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The IP addresses representing the master DNS for this Domain.</p></li>
<li><p><strong>refresh_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>retry_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>soa_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Start of Authority email address. This is required for master Domains.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to control whether this Domain is currently being rendered (defaults to “active”).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
<li><p><strong>ttl_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.axfr_ips">
<em class="property">property </em><code class="sig-name descname">axfr_ips</code><a class="headerlink" href="#pulumi_linode.Domain.axfr_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_linode.Domain.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this Domain. This is for display purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_linode.Domain.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.expire_sec">
<em class="property">property </em><code class="sig-name descname">expire_sec</code><a class="headerlink" href="#pulumi_linode.Domain.expire_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_linode.Domain.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The group this Domain belongs to. This is for display purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.master_ips">
<em class="property">property </em><code class="sig-name descname">master_ips</code><a class="headerlink" href="#pulumi_linode.Domain.master_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP addresses representing the master DNS for this Domain.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.refresh_sec">
<em class="property">property </em><code class="sig-name descname">refresh_sec</code><a class="headerlink" href="#pulumi_linode.Domain.refresh_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.retry_sec">
<em class="property">property </em><code class="sig-name descname">retry_sec</code><a class="headerlink" href="#pulumi_linode.Domain.retry_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.soa_email">
<em class="property">property </em><code class="sig-name descname">soa_email</code><a class="headerlink" href="#pulumi_linode.Domain.soa_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Start of Authority email address. This is required for master Domains.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_linode.Domain.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to control whether this Domain is currently being rendered (defaults to “active”).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_linode.Domain.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.ttl_sec">
<em class="property">property </em><code class="sig-name descname">ttl_sec</code><a class="headerlink" href="#pulumi_linode.Domain.ttl_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_linode.Domain.type" title="Permalink to this definition">¶</a></dt>
<dd><p>If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.DomainRecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">DomainRecord</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Domain Record resource.  This can be used to create, modify, and delete Linodes Domain Records.
For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/manager/dns-manager/">DNS Manager</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createDomainRecord">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure a Domain Record attached to a Linode Domain.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foobar_domain</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Domain</span><span class="p">(</span><span class="s2">&quot;foobarDomain&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;foobar.example&quot;</span><span class="p">,</span>
    <span class="n">soa_email</span><span class="o">=</span><span class="s2">&quot;example@foobar.example&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;master&quot;</span><span class="p">)</span>
<span class="n">foobar_domain_record</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">DomainRecord</span><span class="p">(</span><span class="s2">&quot;foobarDomainRecord&quot;</span><span class="p">,</span>
    <span class="n">domain_id</span><span class="o">=</span><span class="n">foobar_domain</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;www&quot;</span><span class="p">,</span>
    <span class="n">record_type</span><span class="o">=</span><span class="s2">&quot;CNAME&quot;</span><span class="p">,</span>
    <span class="n">target</span><span class="o">=</span><span class="s2">&quot;foobar.example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports no additional attributes.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Domain to access.  <em>Changing ``domain_id`` forces the creation of a new Linode Domain Record.</em>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Record. Setting this is invalid for <code class="docutils literal notranslate"><span class="pre">SRV</span></code> records as it is generated by the API. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the subdomain being associated with an IP address.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port this Record points to.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the target host. Lower values are preferred.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol this Record’s service communicates with. Only valid for SRV records.</p></li>
<li><p><strong>record_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. <em>Changing ``record_type`` forces the creation of a new Linode Domain Record.</em>.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service this Record identified. Only valid for SRV records.</p></li>
<li><p><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag portion of a CAA record. It is invalid to set this on other record types.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target for this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.</p></li>
<li><p><strong>ttl_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The relative weight of this Record. Higher values are preferred.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.DomainRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.domain_record.DomainRecord<a class="headerlink" href="#pulumi_linode.DomainRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Domain to access.  <em>Changing ``domain_id`` forces the creation of a new Linode Domain Record.</em>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Record. Setting this is invalid for <code class="docutils literal notranslate"><span class="pre">SRV</span></code> records as it is generated by the API. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the subdomain being associated with an IP address.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port this Record points to.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the target host. Lower values are preferred.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol this Record’s service communicates with. Only valid for SRV records.</p></li>
<li><p><strong>record_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. <em>Changing ``record_type`` forces the creation of a new Linode Domain Record.</em>.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service this Record identified. Only valid for SRV records.</p></li>
<li><p><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag portion of a CAA record. It is invalid to set this on other record types.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target for this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.</p></li>
<li><p><strong>ttl_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The relative weight of this Record. Higher values are preferred.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.domain_id">
<em class="property">property </em><code class="sig-name descname">domain_id</code><a class="headerlink" href="#pulumi_linode.DomainRecord.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Domain to access.  <em>Changing ``domain_id`` forces the creation of a new Linode Domain Record.</em>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_linode.DomainRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Record. Setting this is invalid for <code class="docutils literal notranslate"><span class="pre">SRV</span></code> records as it is generated by the API. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the subdomain being associated with an IP address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.port">
<em class="property">property </em><code class="sig-name descname">port</code><a class="headerlink" href="#pulumi_linode.DomainRecord.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port this Record points to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_linode.DomainRecord.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the target host. Lower values are preferred.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_linode.DomainRecord.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol this Record’s service communicates with. Only valid for SRV records.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.record_type">
<em class="property">property </em><code class="sig-name descname">record_type</code><a class="headerlink" href="#pulumi_linode.DomainRecord.record_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. <em>Changing ``record_type`` forces the creation of a new Linode Domain Record.</em>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_linode.DomainRecord.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The service this Record identified. Only valid for SRV records.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.tag">
<em class="property">property </em><code class="sig-name descname">tag</code><a class="headerlink" href="#pulumi_linode.DomainRecord.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag portion of a CAA record. It is invalid to set this on other record types.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.target">
<em class="property">property </em><code class="sig-name descname">target</code><a class="headerlink" href="#pulumi_linode.DomainRecord.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The target for this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.ttl_sec">
<em class="property">property </em><code class="sig-name descname">ttl_sec</code><a class="headerlink" href="#pulumi_linode.DomainRecord.ttl_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.weight">
<em class="property">property </em><code class="sig-name descname">weight</code><a class="headerlink" href="#pulumi_linode.DomainRecord.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>The relative weight of this Record. Higher values are preferred.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.DomainRecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.Firewall">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Firewall</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inbounds</span><span class="p">:</span> <span class="n">Union[List[Union[FirewallInboundArgs, Mapping[str, Any], Awaitable[Union[FirewallInboundArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[FirewallInboundArgs, Mapping[str, Any], Awaitable[Union[FirewallInboundArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linodes</span><span class="p">:</span> <span class="n">Union[List[Union[float, Awaitable[float], Output[T]]], Awaitable[List[Union[float, Awaitable[float], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">outbounds</span><span class="p">:</span> <span class="n">Union[List[Union[FirewallOutboundArgs, Mapping[str, Any], Awaitable[Union[FirewallOutboundArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[FirewallOutboundArgs, Mapping[str, Any], Awaitable[Union[FirewallOutboundArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>NOTICE:</strong> The Firewall feature is currently available through early access.</p>
</div></blockquote>
<p>Manages a Linode Firewall.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">my_instance</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;myInstance&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;my_instance&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;linode/ubuntu18.04&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-standard-1&quot;</span><span class="p">,</span>
    <span class="n">root_pass</span><span class="o">=</span><span class="s2">&quot;bogusPassword$&quot;</span><span class="p">,</span>
    <span class="n">swap_size</span><span class="o">=</span><span class="mi">256</span><span class="p">)</span>
<span class="n">my_firewall</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Firewall</span><span class="p">(</span><span class="s2">&quot;myFirewall&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;my_firewall&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">],</span>
    <span class="n">inbounds</span><span class="o">=</span><span class="p">[</span><span class="n">linode</span><span class="o">.</span><span class="n">FirewallInboundArgs</span><span class="p">(</span>
        <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;TCP&quot;</span><span class="p">,</span>
        <span class="n">ports</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;80&quot;</span><span class="p">],</span>
        <span class="n">addresses</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">outbounds</span><span class="o">=</span><span class="p">[</span><span class="n">linode</span><span class="o">.</span><span class="n">FirewallOutboundArgs</span><span class="p">(</span>
        <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;TCP&quot;</span><span class="p">,</span>
        <span class="n">ports</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;80&quot;</span><span class="p">],</span>
        <span class="n">addresses</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">linodes</span><span class="o">=</span><span class="p">[</span><span class="n">my_instance</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the Firewall’s rules are not enforced (defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>inbounds</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'FirewallInboundArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A firewall rule that specifies what inbound network traffic is allowed.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Firewall’s unique label.</p></li>
<li><p><strong>linodes</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>float</em><em>]</em><em>]</em><em>]</em>) – A list of IDs of Linodes this Firewall should govern it’s network traffic for.</p></li>
<li><p><strong>outbounds</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'FirewallOutboundArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A firewall rule that specifies what outbound network traffic is allowed.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.Firewall.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices</span><span class="p">:</span> <span class="n">Union[List[Union[FirewallDeviceArgs, Mapping[str, Any], Awaitable[Union[FirewallDeviceArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[FirewallDeviceArgs, Mapping[str, Any], Awaitable[Union[FirewallDeviceArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inbounds</span><span class="p">:</span> <span class="n">Union[List[Union[FirewallInboundArgs, Mapping[str, Any], Awaitable[Union[FirewallInboundArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[FirewallInboundArgs, Mapping[str, Any], Awaitable[Union[FirewallInboundArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linodes</span><span class="p">:</span> <span class="n">Union[List[Union[float, Awaitable[float], Output[T]]], Awaitable[List[Union[float, Awaitable[float], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">outbounds</span><span class="p">:</span> <span class="n">Union[List[Union[FirewallOutboundArgs, Mapping[str, Any], Awaitable[Union[FirewallOutboundArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[FirewallOutboundArgs, Mapping[str, Any], Awaitable[Union[FirewallOutboundArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.firewall.Firewall<a class="headerlink" href="#pulumi_linode.Firewall.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Firewall resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'FirewallDeviceArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The devices associated with this firewall.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the Firewall’s rules are not enforced (defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>inbounds</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'FirewallInboundArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A firewall rule that specifies what inbound network traffic is allowed.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Firewall’s unique label.</p></li>
<li><p><strong>linodes</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>float</em><em>]</em><em>]</em><em>]</em>) – A list of IDs of Linodes this Firewall should govern it’s network traffic for.</p></li>
<li><p><strong>outbounds</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'FirewallOutboundArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A firewall rule that specifies what outbound network traffic is allowed.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Firewall.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.devices">
<em class="property">property </em><code class="sig-name descname">devices</code><a class="headerlink" href="#pulumi_linode.Firewall.devices" title="Permalink to this definition">¶</a></dt>
<dd><p>The devices associated with this firewall.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_linode.Firewall.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the Firewall’s rules are not enforced (defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.inbounds">
<em class="property">property </em><code class="sig-name descname">inbounds</code><a class="headerlink" href="#pulumi_linode.Firewall.inbounds" title="Permalink to this definition">¶</a></dt>
<dd><p>A firewall rule that specifies what inbound network traffic is allowed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.Firewall.label" title="Permalink to this definition">¶</a></dt>
<dd><p>This Firewall’s unique label.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.linodes">
<em class="property">property </em><code class="sig-name descname">linodes</code><a class="headerlink" href="#pulumi_linode.Firewall.linodes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IDs of Linodes this Firewall should govern it’s network traffic for.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.outbounds">
<em class="property">property </em><code class="sig-name descname">outbounds</code><a class="headerlink" href="#pulumi_linode.Firewall.outbounds" title="Permalink to this definition">¶</a></dt>
<dd><p>A firewall rule that specifies what outbound network traffic is allowed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_linode.Firewall.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Firewall.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_linode.Firewall.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Firewall.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Firewall.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address1</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zip</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="py method">
<dt id="pulumi_linode.GetAccountResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_linode.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetDomainRecordResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetDomainRecordResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetDomainRecordResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomainRecord.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetDomainResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetDomainResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">axfr_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expire_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">soa_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetDomainResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomain.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vendor</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetInstanceTypeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetInstanceTypeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">class_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_out</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transfer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vcpus</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetInstanceTypeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceType.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetNetworkingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetNetworkingIpResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rdns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_mask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetNetworkingIpResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkingIp.</p>
<dl class="py method">
<dt id="pulumi_linode.GetNetworkingIpResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_linode.GetNetworkingIpResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetObjectStorageClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetObjectStorageClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_site_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetObjectStorageClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getObjectStorageCluster.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetProfileResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorized_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lish_auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">referrals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restricted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">two_factor_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProfile.</p>
<dl class="py method">
<dt id="pulumi_linode.GetProfileResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_linode.GetProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetRegionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetRegionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetRegionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegion.</p>
<dl class="py method">
<dt id="pulumi_linode.GetRegionResult.country">
<em class="property">property </em><code class="sig-name descname">country</code><a class="headerlink" href="#pulumi_linode.GetRegionResult.country" title="Permalink to this definition">¶</a></dt>
<dd><p>The country the region resides in.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKey.</p>
<dl class="py method">
<dt id="pulumi_linode.GetSshKeyResult.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_linode.GetSshKeyResult.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this key was added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.GetSshKeyResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_linode.GetSshKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.GetSshKeyResult.ssh_key">
<em class="property">property </em><code class="sig-name descname">ssh_key</code><a class="headerlink" href="#pulumi_linode.GetSshKeyResult.ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetStackScriptResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetStackScriptResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployments_active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployments_total</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rev_note</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_gravatar_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetStackScriptResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStackScript.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restricted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="py method">
<dt id="pulumi_linode.GetUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_linode.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filesystem_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.Image">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Image resource.  This can be used to create, modify, and delete Linodes Images.  Linode Images are snapshots of a Linode Instance Disk which can then be used to provision more Linode Instances.  Images can be used across regions.</p>
<p>For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/disk-images/linode-images/">Linode’s documentation on Images</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createImage">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to create an Image from a Linode Instance Disk and then deploy a new Linode Instance in another region using that Image.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-central&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-nanode-1&quot;</span><span class="p">)</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Image</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Image taken from foo&quot;</span><span class="p">,</span>
    <span class="n">disk_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">disks</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;foo-sda-image&quot;</span><span class="p">,</span>
    <span class="n">linode_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">bar_based</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;barBased&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="n">bar</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;eu-west&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">type</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The unique ID of this Image.  The ID of private images begin with <code class="docutils literal notranslate"><span class="pre">private/</span></code> followed by the numeric identifier of the private image, for example <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created</span></code> - When this Image was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created_by</span></code> - The name of the User who created this Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deprecated</span></code> - Whether or not this Image is deprecated. Will only be True for deprecated public Images.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_public</span></code> - True if the Image is public.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> - The minimum size this Image needs to deploy. Size is in MB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - How the Image was created. ‘Manual’ Images can be created at any time. ‘Automatic’ images are created automatically from a deleted Linode.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> - Only Images created automatically (from a deleted Linode; type=automatic) will expire.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vendor</span></code> - The upstream distribution vendor. Nil for private Images.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A detailed description of this Image.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Linode Disk that this Image will be created from.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the Image. Labels cannot contain special characters.</p></li>
<li><p><strong>linode_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Linode that this Image will be created from.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.Image.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprecated</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vendor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.image.Image<a class="headerlink" href="#pulumi_linode.Image.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Image resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When this Image was created.</p></li>
<li><p><strong>created_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the User who created this Image.</p></li>
<li><p><strong>deprecated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this Image is deprecated. Will only be True for deprecated public Images.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A detailed description of this Image.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Linode Disk that this Image will be created from.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Only Images created automatically (from a deleted Linode; type=automatic) will expire.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True if the Image is public.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the Image. Labels cannot contain special characters.</p></li>
<li><p><strong>linode_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Linode that this Image will be created from.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum size this Image needs to deploy. Size is in MB.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How the Image was created. ‘Manual’ Images can be created at any time. ‘Automatic’ images are created automatically from
a deleted Linode.</p></li>
<li><p><strong>vendor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The upstream distribution vendor. Nil for private Images.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_linode.Image.created" title="Permalink to this definition">¶</a></dt>
<dd><p>When this Image was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.created_by">
<em class="property">property </em><code class="sig-name descname">created_by</code><a class="headerlink" href="#pulumi_linode.Image.created_by" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the User who created this Image.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.deprecated">
<em class="property">property </em><code class="sig-name descname">deprecated</code><a class="headerlink" href="#pulumi_linode.Image.deprecated" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this Image is deprecated. Will only be True for deprecated public Images.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_linode.Image.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A detailed description of this Image.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.disk_id">
<em class="property">property </em><code class="sig-name descname">disk_id</code><a class="headerlink" href="#pulumi_linode.Image.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Linode Disk that this Image will be created from.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.expiry">
<em class="property">property </em><code class="sig-name descname">expiry</code><a class="headerlink" href="#pulumi_linode.Image.expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>Only Images created automatically (from a deleted Linode; type=automatic) will expire.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.is_public">
<em class="property">property </em><code class="sig-name descname">is_public</code><a class="headerlink" href="#pulumi_linode.Image.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>True if the Image is public.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.Image.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the Image. Labels cannot contain special characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.linode_id">
<em class="property">property </em><code class="sig-name descname">linode_id</code><a class="headerlink" href="#pulumi_linode.Image.linode_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Linode that this Image will be created from.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_linode.Image.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size this Image needs to deploy. Size is in MB.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_linode.Image.type" title="Permalink to this definition">¶</a></dt>
<dd><p>How the Image was created. ‘Manual’ Images can be created at any time. ‘Automatic’ images are created automatically from
a deleted Linode.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.vendor">
<em class="property">property </em><code class="sig-name descname">vendor</code><a class="headerlink" href="#pulumi_linode.Image.vendor" title="Permalink to this definition">¶</a></dt>
<dd><p>The upstream distribution vendor. Nil for private Images.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Image.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alerts</span><span class="p">:</span> <span class="n">Union[InstanceAlertsArgs, Mapping[str, Any], Awaitable[Union[InstanceAlertsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_keys</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_users</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boot_config_label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configs</span><span class="p">:</span> <span class="n">Union[List[Union[InstanceConfigArgs, Mapping[str, Any], Awaitable[Union[InstanceConfigArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[InstanceConfigArgs, Mapping[str, Any], Awaitable[Union[InstanceConfigArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="p">:</span> <span class="n">Union[List[Union[InstanceDiskArgs, Mapping[str, Any], Awaitable[Union[InstanceDiskArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[InstanceDiskArgs, Mapping[str, Any], Awaitable[Union[InstanceDiskArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_pass</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stackscript_data</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stackscript_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">swap_size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">watchdog_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Instance resource.  This can be used to create, modify, and delete Linodes.
For more information, see <a class="reference external" href="https://linode.com/docs/getting-started/">Getting Started with Linode</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createLinodeInstance">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure a Linode instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">web</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;web&quot;</span><span class="p">,</span>
    <span class="n">authorized_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ssh-rsa AAAA...Gw== user@example.local&quot;</span><span class="p">],</span>
    <span class="n">group</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;linode/ubuntu18.04&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;simple_instance&quot;</span><span class="p">,</span>
    <span class="n">private_ip</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-central&quot;</span><span class="p">,</span>
    <span class="n">root_pass</span><span class="o">=</span><span class="s2">&quot;terr4form-test&quot;</span><span class="p">,</span>
    <span class="n">swap_size</span><span class="o">=</span><span class="mi">256</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-standard-1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Using explicit Instance Configs and Disks it is possible to create a more elaborate Linode instance.  This can be used to provision multiple disks and volumes during Instance creation.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">me</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_profile</span><span class="p">()</span>
<span class="n">web_volume</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;webVolume&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;web_volume&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-central&quot;</span><span class="p">,</span>
    <span class="n">size</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
<span class="n">web</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;web&quot;</span><span class="p">,</span>
    <span class="n">boot_config_label</span><span class="o">=</span><span class="s2">&quot;boot_config&quot;</span><span class="p">,</span>
    <span class="n">configs</span><span class="o">=</span><span class="p">[</span><span class="n">linode</span><span class="o">.</span><span class="n">InstanceConfigArgs</span><span class="p">(</span>
        <span class="n">devices</span><span class="o">=</span><span class="n">linode</span><span class="o">.</span><span class="n">InstanceConfigDevicesArgs</span><span class="p">(</span>
            <span class="n">sda</span><span class="o">=</span><span class="n">linode</span><span class="o">.</span><span class="n">InstanceConfigDevicesSdaArgs</span><span class="p">(</span>
                <span class="n">disk_label</span><span class="o">=</span><span class="s2">&quot;boot&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">sdb</span><span class="o">=</span><span class="n">linode</span><span class="o">.</span><span class="n">InstanceConfigDevicesSdbArgs</span><span class="p">(</span>
                <span class="n">volume_id</span><span class="o">=</span><span class="n">web_volume</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">kernel</span><span class="o">=</span><span class="s2">&quot;linode/latest-64bit&quot;</span><span class="p">,</span>
        <span class="n">label</span><span class="o">=</span><span class="s2">&quot;boot_config&quot;</span><span class="p">,</span>
        <span class="n">root_device</span><span class="o">=</span><span class="s2">&quot;/dev/sda&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">disks</span><span class="o">=</span><span class="p">[</span><span class="n">linode</span><span class="o">.</span><span class="n">InstanceDiskArgs</span><span class="p">(</span>
        <span class="n">authorized_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ssh-rsa AAAA...Gw== user@example.local&quot;</span><span class="p">],</span>
        <span class="n">authorized_users</span><span class="o">=</span><span class="p">[</span><span class="n">me</span><span class="o">.</span><span class="n">username</span><span class="p">],</span>
        <span class="n">image</span><span class="o">=</span><span class="s2">&quot;linode/ubuntu18.04&quot;</span><span class="p">,</span>
        <span class="n">label</span><span class="o">=</span><span class="s2">&quot;boot&quot;</span><span class="p">,</span>
        <span class="n">root_pass</span><span class="o">=</span><span class="s2">&quot;terr4form-test&quot;</span><span class="p">,</span>
        <span class="n">size</span><span class="o">=</span><span class="mi">3000</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">group</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;complex_instance&quot;</span><span class="p">,</span>
    <span class="n">private_ip</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-central&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-nanode-1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>This Linode Instance resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - The status of the instance, indicating the current readiness state. (<code class="docutils literal notranslate"><span class="pre">running</span></code>, <code class="docutils literal notranslate"><span class="pre">offline</span></code>, …)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> - A string containing the Linode’s public IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> - This Linode’s Private IPv4 Address, if enabled.  The regional private IP address range, 192.168.128.0/17, is shared by all Linode Instances in a region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> - This Linode’s IPv6 SLAAC addresses. This address is specific to a Linode, and may not be shared.  The prefix (<code class="docutils literal notranslate"><span class="pre">/64</span></code>) is included in this attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4</span></code> - This Linode’s IPv4 Addresses. Each Linode is assigned a single public IPv4 address upon creation, and may get a single private IPv4 address if needed. You may need to open a support ticket to get additional IPv4 addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">specs.0.disk</span></code> -  The amount of storage space, in GB. this Linode has access to. A typical Linode will divide this space between a primary disk with an image deployed to it, and a swap disk, usually 512 MB. This is the default configuration created when deploying a Linode with an image through POST /linode/instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">specs.0.memory</span></code> - The amount of RAM, in MB, this Linode has access to. Typically a Linode will choose to boot with all of its available RAM, but this can be configured in a Config profile.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">specs.0.vcpus</span></code> - The number of vcpus this Linode has access to. Typically a Linode will choose to boot with all of its available vcpus, but this can be configured in a Config Profile.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">specs.0.transfer</span></code> - The amount of network transfer this Linode is allotted each month.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backups</span></code> - Information about this Linode’s backups status.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> - If this Linode has the Backup service enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedule</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> -  The day of the week that your Linode’s weekly Backup is taken. If not set manually, a day will be chosen for you. Backups are taken every day, but backups taken on this day are preferred when selecting backups to retain for a longer period.  If not set manually, then when backups are initially enabled, this may come back as “Scheduling” until the day is automatically selected.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> - The window (‘W0’-‘W22’) in which your backups will be taken, in UTC. A backups window is a two-hour span of time in which the backup may occur. For example, ‘W10’ indicates that your backups should be taken between 10:00 and 12:00. If you do not choose a backup window, one will be selected for you automatically.  If not set manually, when backups are initially enabled this may come back as Scheduling until the window is automatically selected.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_keys</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>authorized_users</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>backup_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A Backup ID from another Linode’s available backups. Your User must have read_write access to that Linode, the Backup must have a status of successful, and the Linode must be deployed to the same region as the Backup. See /linode/instances/{linodeId}/backups for a Linode’s available backups. This field and the image field are mutually exclusive. <em>This value can not be imported.</em> <em>Changing ``backup_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>backups_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.</p></li>
<li><p><strong>boot_config_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em></p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InstanceConfigArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Configuration profiles define the VM settings and boot behavior of the Linode Instance.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display group of the Linode instance.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. See all images <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc. See all regions <a class="reference external" href="https://api.linode.com/v4/regions">here</a>. <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.</p>
</p></li>
<li><p><strong>root_pass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The initial password for the <code class="docutils literal notranslate"><span class="pre">root</span></code> user account. <em>This value can not be imported.</em> <em>Changing ``root_pass`` forces the creation of a new Linode Instance.</em> <em>If omitted, a random password will be generated but will not be stored in state.</em></p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>stackscript_data</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>stackscript_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>swap_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Linode type defines the pricing, CPU, disk, and RAM specs of the instance. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc. See all types <a class="reference external" href="https://api.linode.com/v4/linode/types">here</a>.</p>
</p></li>
<li><p><strong>watchdog_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alerts</span><span class="p">:</span> <span class="n">Union[InstanceAlertsArgs, Mapping[str, Any], Awaitable[Union[InstanceAlertsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_keys</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_users</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="p">:</span> <span class="n">Union[InstanceBackupsArgs, Mapping[str, Any], Awaitable[Union[InstanceBackupsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boot_config_label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configs</span><span class="p">:</span> <span class="n">Union[List[Union[InstanceConfigArgs, Mapping[str, Any], Awaitable[Union[InstanceConfigArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[InstanceConfigArgs, Mapping[str, Any], Awaitable[Union[InstanceConfigArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="p">:</span> <span class="n">Union[List[Union[InstanceDiskArgs, Mapping[str, Any], Awaitable[Union[InstanceDiskArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[InstanceDiskArgs, Mapping[str, Any], Awaitable[Union[InstanceDiskArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4s</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_pass</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">specs</span><span class="p">:</span> <span class="n">Union[InstanceSpecsArgs, Mapping[str, Any], Awaitable[Union[InstanceSpecsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stackscript_data</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stackscript_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">swap_size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">watchdog_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.instance.Instance<a class="headerlink" href="#pulumi_linode.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_keys</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>authorized_users</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>backup_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A Backup ID from another Linode’s available backups. Your User must have read_write access to that Linode, the Backup must have a status of successful, and the Linode must be deployed to the same region as the Backup. See /linode/instances/{linodeId}/backups for a Linode’s available backups. This field and the image field are mutually exclusive. <em>This value can not be imported.</em> <em>Changing ``backup_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>backups</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InstanceBackupsArgs'</em><em>]</em><em>]</em>) – Information about this Linode’s backups status.</p></li>
<li><p><strong>backups_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.</p></li>
<li><p><strong>boot_config_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em></p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InstanceConfigArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Configuration profiles define the VM settings and boot behavior of the Linode Instance.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display group of the Linode instance.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. See all images <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p>
</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Linode’s Public IPv4 Address. If there are multiple public IPv4 addresses on this Instance, an arbitrary address
will be used for this field.</p></li>
<li><p><strong>ipv4s</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – This Linode’s IPv4 Addresses. Each Linode is assigned a single public IPv4 address upon creation, and may get a single
private IPv4 address if needed. You may need to open a support ticket to get additional IPv4 addresses.</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Linode’s IPv6 SLAAC addresses. This address is specific to a Linode, and may not be shared.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Linode’s Private IPv4 Address. The regional private IP address range is 192.168.128/17 address shared by all Linode
Instances in a region.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc. See all regions <a class="reference external" href="https://api.linode.com/v4/regions">here</a>. <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.</p>
</p></li>
<li><p><strong>root_pass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The initial password for the <code class="docutils literal notranslate"><span class="pre">root</span></code> user account. <em>This value can not be imported.</em> <em>Changing ``root_pass`` forces the creation of a new Linode Instance.</em> <em>If omitted, a random password will be generated but will not be stored in state.</em></p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>stackscript_data</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>stackscript_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the instance, indicating the current readiness state.</p></li>
<li><p><strong>swap_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Linode type defines the pricing, CPU, disk, and RAM specs of the instance. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc. See all types <a class="reference external" href="https://api.linode.com/v4/linode/types">here</a>.</p>
</p></li>
<li><p><strong>watchdog_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.authorized_keys">
<em class="property">property </em><code class="sig-name descname">authorized_keys</code><a class="headerlink" href="#pulumi_linode.Instance.authorized_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.authorized_users">
<em class="property">property </em><code class="sig-name descname">authorized_users</code><a class="headerlink" href="#pulumi_linode.Instance.authorized_users" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.backup_id">
<em class="property">property </em><code class="sig-name descname">backup_id</code><a class="headerlink" href="#pulumi_linode.Instance.backup_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A Backup ID from another Linode’s available backups. Your User must have read_write access to that Linode, the Backup must have a status of successful, and the Linode must be deployed to the same region as the Backup. See /linode/instances/{linodeId}/backups for a Linode’s available backups. This field and the image field are mutually exclusive. <em>This value can not be imported.</em> <em>Changing ``backup_id`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.backups">
<em class="property">property </em><code class="sig-name descname">backups</code><a class="headerlink" href="#pulumi_linode.Instance.backups" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about this Linode’s backups status.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.backups_enabled">
<em class="property">property </em><code class="sig-name descname">backups_enabled</code><a class="headerlink" href="#pulumi_linode.Instance.backups_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.boot_config_label">
<em class="property">property </em><code class="sig-name descname">boot_config_label</code><a class="headerlink" href="#pulumi_linode.Instance.boot_config_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.configs">
<em class="property">property </em><code class="sig-name descname">configs</code><a class="headerlink" href="#pulumi_linode.Instance.configs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration profiles define the VM settings and boot behavior of the Linode Instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_linode.Instance.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The display group of the Linode instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.image">
<em class="property">property </em><code class="sig-name descname">image</code><a class="headerlink" href="#pulumi_linode.Instance.image" title="Permalink to this definition">¶</a></dt>
<dd><p>An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. See all images <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.ip_address">
<em class="property">property </em><code class="sig-name descname">ip_address</code><a class="headerlink" href="#pulumi_linode.Instance.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>This Linode’s Public IPv4 Address. If there are multiple public IPv4 addresses on this Instance, an arbitrary address
will be used for this field.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.ipv4s">
<em class="property">property </em><code class="sig-name descname">ipv4s</code><a class="headerlink" href="#pulumi_linode.Instance.ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>This Linode’s IPv4 Addresses. Each Linode is assigned a single public IPv4 address upon creation, and may get a single
private IPv4 address if needed. You may need to open a support ticket to get additional IPv4 addresses.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.ipv6">
<em class="property">property </em><code class="sig-name descname">ipv6</code><a class="headerlink" href="#pulumi_linode.Instance.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>This Linode’s IPv6 SLAAC addresses. This address is specific to a Linode, and may not be shared.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.Instance.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.private_ip">
<em class="property">property </em><code class="sig-name descname">private_ip</code><a class="headerlink" href="#pulumi_linode.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.private_ip_address">
<em class="property">property </em><code class="sig-name descname">private_ip_address</code><a class="headerlink" href="#pulumi_linode.Instance.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>This Linode’s Private IPv4 Address. The regional private IP address range is 192.168.128/17 address shared by all Linode
Instances in a region.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_linode.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc. See all regions <a class="reference external" href="https://api.linode.com/v4/regions">here</a>. <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.root_pass">
<em class="property">property </em><code class="sig-name descname">root_pass</code><a class="headerlink" href="#pulumi_linode.Instance.root_pass" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial password for the <code class="docutils literal notranslate"><span class="pre">root</span></code> user account. <em>This value can not be imported.</em> <em>Changing ``root_pass`` forces the creation of a new Linode Instance.</em> <em>If omitted, a random password will be generated but will not be stored in state.</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.stackscript_data">
<em class="property">property </em><code class="sig-name descname">stackscript_data</code><a class="headerlink" href="#pulumi_linode.Instance.stackscript_data" title="Permalink to this definition">¶</a></dt>
<dd><p>An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.stackscript_id">
<em class="property">property </em><code class="sig-name descname">stackscript_id</code><a class="headerlink" href="#pulumi_linode.Instance.stackscript_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_linode.Instance.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the instance, indicating the current readiness state.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.swap_size">
<em class="property">property </em><code class="sig-name descname">swap_size</code><a class="headerlink" href="#pulumi_linode.Instance.swap_size" title="Permalink to this definition">¶</a></dt>
<dd><p>When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_linode.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_linode.Instance.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Linode type defines the pricing, CPU, disk, and RAM specs of the instance. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc. See all types <a class="reference external" href="https://api.linode.com/v4/linode/types">here</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.watchdog_enabled">
<em class="property">property </em><code class="sig-name descname">watchdog_enabled</code><a class="headerlink" href="#pulumi_linode.Instance.watchdog_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.LkeCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">LkeCluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">k8s_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pools</span><span class="p">:</span> <span class="n">Union[List[Union[LkeClusterPoolArgs, Mapping[str, Any], Awaitable[Union[LkeClusterPoolArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LkeClusterPoolArgs, Mapping[str, Any], Awaitable[Union[LkeClusterPoolArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.LkeCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an LKE cluster.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">LkeCluster</span><span class="p">(</span><span class="s2">&quot;my-cluster&quot;</span><span class="p">,</span>
    <span class="n">k8s_version</span><span class="o">=</span><span class="s2">&quot;1.17&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;my-cluster&quot;</span><span class="p">,</span>
    <span class="n">pools</span><span class="o">=</span><span class="p">[</span><span class="n">linode</span><span class="o">.</span><span class="n">LkeClusterPoolArgs</span><span class="p">(</span>
        <span class="n">count</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-standard-2&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-central&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;prod&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>k8s_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired Kubernetes version for this Kubernetes cluster in the format of <code class="docutils literal notranslate"><span class="pre">major.minor</span></code> (e.g. <code class="docutils literal notranslate"><span class="pre">1.17</span></code>), and the latest supported patch version will be deployed.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Kubernetes cluster’s unique label.</p></li>
<li><p><strong>pools</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LkeClusterPoolArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Additional nested attributes:</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Kubernetes cluster’s location.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.LkeCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_endpoints</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">k8s_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pools</span><span class="p">:</span> <span class="n">Union[List[Union[LkeClusterPoolArgs, Mapping[str, Any], Awaitable[Union[LkeClusterPoolArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LkeClusterPoolArgs, Mapping[str, Any], Awaitable[Union[LkeClusterPoolArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.lke_cluster.LkeCluster<a class="headerlink" href="#pulumi_linode.LkeCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LkeCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The endpoints for the Kubernetes API server.</p></li>
<li><p><strong>k8s_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired Kubernetes version for this Kubernetes cluster in the format of <code class="docutils literal notranslate"><span class="pre">major.minor</span></code> (e.g. <code class="docutils literal notranslate"><span class="pre">1.17</span></code>), and the latest supported patch version will be deployed.</p></li>
<li><p><strong>kubeconfig</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 encoded kubeconfig for the Kubernetes cluster.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Kubernetes cluster’s unique label.</p></li>
<li><p><strong>pools</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LkeClusterPoolArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Additional nested attributes:</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Kubernetes cluster’s location.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the node.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.api_endpoints">
<em class="property">property </em><code class="sig-name descname">api_endpoints</code><a class="headerlink" href="#pulumi_linode.LkeCluster.api_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoints for the Kubernetes API server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.k8s_version">
<em class="property">property </em><code class="sig-name descname">k8s_version</code><a class="headerlink" href="#pulumi_linode.LkeCluster.k8s_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired Kubernetes version for this Kubernetes cluster in the format of <code class="docutils literal notranslate"><span class="pre">major.minor</span></code> (e.g. <code class="docutils literal notranslate"><span class="pre">1.17</span></code>), and the latest supported patch version will be deployed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.kubeconfig">
<em class="property">property </em><code class="sig-name descname">kubeconfig</code><a class="headerlink" href="#pulumi_linode.LkeCluster.kubeconfig" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 encoded kubeconfig for the Kubernetes cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.LkeCluster.label" title="Permalink to this definition">¶</a></dt>
<dd><p>This Kubernetes cluster’s unique label.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.pools">
<em class="property">property </em><code class="sig-name descname">pools</code><a class="headerlink" href="#pulumi_linode.LkeCluster.pools" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional nested attributes:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_linode.LkeCluster.region" title="Permalink to this definition">¶</a></dt>
<dd><p>This Kubernetes cluster’s location.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_linode.LkeCluster.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the node.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_linode.LkeCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.LkeCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.LkeCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.LkeCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.NodeBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_conn_throttle</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode NodeBalancer resource.  This can be used to create, modify, and delete Linodes NodeBalancers in Linode’s managed load balancer service.
For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/nodebalancer/getting-started-with-nodebalancers/">Getting Started with NodeBalancers</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createNodeBalancer">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure a NodeBalancer.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foobar</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">NodeBalancer</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">client_conn_throttle</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;mynodebalancer&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foobar&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> - This NodeBalancer’s hostname, ending with .nodebalancer.linode.com</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4</span></code> - The Public IPv4 Address of this NodeBalancer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> - The Public IPv6 Address of this NodeBalancer</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_conn_throttle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Throttle connections per second (0-20). Set to 0 (default) to disable throttling.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode NodeBalancer</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this NodeBalancer will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode NodeBalancer.</em>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_conn_throttle</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transfer</span><span class="p">:</span> <span class="n">Union[NodeBalancerTransferArgs, Mapping[str, Any], Awaitable[Union[NodeBalancerTransferArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.node_balancer.NodeBalancer<a class="headerlink" href="#pulumi_linode.NodeBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_conn_throttle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Throttle connections per second (0-20). Set to 0 (default) to disable throttling.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This NodeBalancer’s hostname, ending with .nodebalancer.linode.com</p></li>
<li><p><strong>ipv4</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Public IPv4 Address of this NodeBalancer</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Public IPv6 Address of this NodeBalancer</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode NodeBalancer</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this NodeBalancer will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode NodeBalancer.</em>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.client_conn_throttle">
<em class="property">property </em><code class="sig-name descname">client_conn_throttle</code><a class="headerlink" href="#pulumi_linode.NodeBalancer.client_conn_throttle" title="Permalink to this definition">¶</a></dt>
<dd><p>Throttle connections per second (0-20). Set to 0 (default) to disable throttling.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_linode.NodeBalancer.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>This NodeBalancer’s hostname, ending with .nodebalancer.linode.com</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.ipv4">
<em class="property">property </em><code class="sig-name descname">ipv4</code><a class="headerlink" href="#pulumi_linode.NodeBalancer.ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The Public IPv4 Address of this NodeBalancer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.ipv6">
<em class="property">property </em><code class="sig-name descname">ipv6</code><a class="headerlink" href="#pulumi_linode.NodeBalancer.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>The Public IPv6 Address of this NodeBalancer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.NodeBalancer.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode NodeBalancer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_linode.NodeBalancer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where this NodeBalancer will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode NodeBalancer.</em>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_linode.NodeBalancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.NodeBalancerConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancerConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_attempts</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_body</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_interval</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_passive</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_timeout</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cipher_suite</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodebalancer_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode NodeBalancer Config resource.  This can be used to create, modify, and delete Linodes NodeBalancer Configs.
For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/nodebalancer/getting-started-with-nodebalancers/">Getting Started with NodeBalancers</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createNodeBalancerConfig">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure a NodeBalancer Config attached to a Linode instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foobar</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">NodeBalancer</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">client_conn_throttle</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;mynodebalancer&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">)</span>
<span class="n">foofig</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">NodeBalancerConfig</span><span class="p">(</span><span class="s2">&quot;foofig&quot;</span><span class="p">,</span>
    <span class="n">algorithm</span><span class="o">=</span><span class="s2">&quot;source&quot;</span><span class="p">,</span>
    <span class="n">check</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">check_attempts</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">check_path</span><span class="o">=</span><span class="s2">&quot;/foo&quot;</span><span class="p">,</span>
    <span class="n">check_timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
    <span class="n">nodebalancer_id</span><span class="o">=</span><span class="n">foobar</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">8088</span><span class="p">,</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">stickiness</span><span class="o">=</span><span class="s2">&quot;http_cookie&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ssl_commonname</span></code> - The common name for the SSL certification this port is serving if this port is not configured to use SSL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl_fingerprint</span></code> - The fingerprint for the SSL certification this port is serving if this port is not configured to use SSL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_status_up</span></code> - The number of backends considered to be ‘UP’ and healthy, and that are serving requests.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_status_down</span></code> - The number of backends considered to be ‘DOWN’ and unhealthy. These are not in rotation, and not serving requests.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What algorithm this NodeBalancer should use for routing traffic to backends: roundrobin, leastconn, source</p></li>
<li><p><strong>check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected.</p></li>
<li><p><strong>check_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How many times to attempt a check before considering a backend to be down. (1-30)</p></li>
<li><p><strong>check_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This value must be present in the response body of the check in order for it to pass. If this value is not present in
the response body of a check request, the backend is considered to be down</p></li>
<li><p><strong>check_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in seconds, to check that backends are up and serving requests.</p></li>
<li><p><strong>check_passive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, any response from this backend with a 5xx status code will be enough for it to be considered unhealthy and taken out of rotation.</p></li>
<li><p><strong>check_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.</p></li>
<li><p><strong>check_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long, in seconds, to wait for a check attempt before considering it failed. (1-30)</p></li>
<li><p><strong>cipher_suite</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What ciphers to use for SSL connections served by this NodeBalancer. <code class="docutils literal notranslate"><span class="pre">legacy</span></code> is considered insecure and should only be used if necessary.</p></li>
<li><p><strong>nodebalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the NodeBalancer to access.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TCP port this Config is for. These values must be unique across configs on a single NodeBalancer (you can’t have two configs for port 80, for example). While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. (Defaults to 80)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol this port is configured to serve. If this is set to https you must include an ssl_cert and an ssl_key. (Defaults to “http”)</p></li>
<li><p><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of ProxyProtocol to use for the underlying NodeBalancer. This requires protocol to be <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, and <code class="docutils literal notranslate"><span class="pre">v2</span></code>. (Defaults to <code class="docutils literal notranslate"><span class="pre">none</span></code>)</p></li>
<li><p><strong>ssl_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate this port is serving. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p></li>
<li><p><strong>ssl_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key corresponding to this port’s certificate. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p></li>
<li><p><strong>stickiness</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how session stickiness is handled on this port: ‘none’, ‘table’, ‘http_cookie’</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_attempts</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_body</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_interval</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_passive</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_timeout</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cipher_suite</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_status</span><span class="p">:</span> <span class="n">Union[NodeBalancerConfigNodeStatusArgs, Mapping[str, Any], Awaitable[Union[NodeBalancerConfigNodeStatusArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodebalancer_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_commonname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_fingerprint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.node_balancer_config.NodeBalancerConfig<a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeBalancerConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What algorithm this NodeBalancer should use for routing traffic to backends: roundrobin, leastconn, source</p></li>
<li><p><strong>check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected.</p></li>
<li><p><strong>check_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How many times to attempt a check before considering a backend to be down. (1-30)</p></li>
<li><p><strong>check_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This value must be present in the response body of the check in order for it to pass. If this value is not present in
the response body of a check request, the backend is considered to be down</p></li>
<li><p><strong>check_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in seconds, to check that backends are up and serving requests.</p></li>
<li><p><strong>check_passive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, any response from this backend with a 5xx status code will be enough for it to be considered unhealthy and taken out of rotation.</p></li>
<li><p><strong>check_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.</p></li>
<li><p><strong>check_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long, in seconds, to wait for a check attempt before considering it failed. (1-30)</p></li>
<li><p><strong>cipher_suite</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What ciphers to use for SSL connections served by this NodeBalancer. <code class="docutils literal notranslate"><span class="pre">legacy</span></code> is considered insecure and should only be used if necessary.</p></li>
<li><p><strong>nodebalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the NodeBalancer to access.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TCP port this Config is for. These values must be unique across configs on a single NodeBalancer (you can’t have two configs for port 80, for example). While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. (Defaults to 80)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol this port is configured to serve. If this is set to https you must include an ssl_cert and an ssl_key. (Defaults to “http”)</p></li>
<li><p><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of ProxyProtocol to use for the underlying NodeBalancer. This requires protocol to be <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, and <code class="docutils literal notranslate"><span class="pre">v2</span></code>. (Defaults to <code class="docutils literal notranslate"><span class="pre">none</span></code>)</p></li>
<li><p><strong>ssl_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate this port is serving. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p></li>
<li><p><strong>ssl_commonname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The common name for the SSL certification this port is serving if this port is not configured to use SSL.</p></li>
<li><p><strong>ssl_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint for the SSL certification this port is serving if this port is not configured to use SSL.</p></li>
<li><p><strong>ssl_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key corresponding to this port’s certificate. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p></li>
<li><p><strong>stickiness</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how session stickiness is handled on this port: ‘none’, ‘table’, ‘http_cookie’</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.algorithm">
<em class="property">property </em><code class="sig-name descname">algorithm</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>What algorithm this NodeBalancer should use for routing traffic to backends: roundrobin, leastconn, source</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.check">
<em class="property">property </em><code class="sig-name descname">check</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.check_attempts">
<em class="property">property </em><code class="sig-name descname">check_attempts</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>How many times to attempt a check before considering a backend to be down. (1-30)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.check_body">
<em class="property">property </em><code class="sig-name descname">check_body</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_body" title="Permalink to this definition">¶</a></dt>
<dd><p>This value must be present in the response body of the check in order for it to pass. If this value is not present in
the response body of a check request, the backend is considered to be down</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.check_interval">
<em class="property">property </em><code class="sig-name descname">check_interval</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in seconds, to check that backends are up and serving requests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.check_passive">
<em class="property">property </em><code class="sig-name descname">check_passive</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_passive" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, any response from this backend with a 5xx status code will be enough for it to be considered unhealthy and taken out of rotation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.check_path">
<em class="property">property </em><code class="sig-name descname">check_path</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.check_timeout">
<em class="property">property </em><code class="sig-name descname">check_timeout</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>How long, in seconds, to wait for a check attempt before considering it failed. (1-30)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.cipher_suite">
<em class="property">property </em><code class="sig-name descname">cipher_suite</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.cipher_suite" title="Permalink to this definition">¶</a></dt>
<dd><p>What ciphers to use for SSL connections served by this NodeBalancer. <code class="docutils literal notranslate"><span class="pre">legacy</span></code> is considered insecure and should only be used if necessary.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.nodebalancer_id">
<em class="property">property </em><code class="sig-name descname">nodebalancer_id</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.nodebalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancer to access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.port">
<em class="property">property </em><code class="sig-name descname">port</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The TCP port this Config is for. These values must be unique across configs on a single NodeBalancer (you can’t have two configs for port 80, for example). While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. (Defaults to 80)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol this port is configured to serve. If this is set to https you must include an ssl_cert and an ssl_key. (Defaults to “http”)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.proxy_protocol">
<em class="property">property </em><code class="sig-name descname">proxy_protocol</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.proxy_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of ProxyProtocol to use for the underlying NodeBalancer. This requires protocol to be <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, and <code class="docutils literal notranslate"><span class="pre">v2</span></code>. (Defaults to <code class="docutils literal notranslate"><span class="pre">none</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_cert">
<em class="property">property </em><code class="sig-name descname">ssl_cert</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate this port is serving. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_commonname">
<em class="property">property </em><code class="sig-name descname">ssl_commonname</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_commonname" title="Permalink to this definition">¶</a></dt>
<dd><p>The common name for the SSL certification this port is serving if this port is not configured to use SSL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_fingerprint">
<em class="property">property </em><code class="sig-name descname">ssl_fingerprint</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint for the SSL certification this port is serving if this port is not configured to use SSL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_key">
<em class="property">property </em><code class="sig-name descname">ssl_key</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key corresponding to this port’s certificate. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.stickiness">
<em class="property">property </em><code class="sig-name descname">stickiness</code><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.stickiness" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls how session stickiness is handled on this port: ‘none’, ‘table’, ‘http_cookie’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancerConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.NodeBalancerNode">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancerNode</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodebalancer_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode NodeBalancer Node resource.  This can be used to create, modify, and delete Linodes NodeBalancer Nodes.
For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/nodebalancer/getting-started-with-nodebalancers/">Getting Started with NodeBalancers</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createNodeBalancerNode">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure NodeBalancer Nodes attached to Linode instances.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">web</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">)]:</span>
    <span class="n">web</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;web-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">authorized_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ssh-rsa AAAA...Gw== user@example.local&quot;</span><span class="p">],</span>
        <span class="n">image</span><span class="o">=</span><span class="s2">&quot;linode/ubuntu18.04&quot;</span><span class="p">,</span>
        <span class="n">label</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;web-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">private_ip</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">,</span>
        <span class="n">root_pass</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-standard-1&quot;</span><span class="p">))</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">NodeBalancer</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">client_conn_throttle</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;mynodebalancer&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">)</span>
<span class="n">foofig</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">NodeBalancerConfig</span><span class="p">(</span><span class="s2">&quot;foofig&quot;</span><span class="p">,</span>
    <span class="n">algorithm</span><span class="o">=</span><span class="s2">&quot;source&quot;</span><span class="p">,</span>
    <span class="n">check</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">check_attempts</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">check_path</span><span class="o">=</span><span class="s2">&quot;/foo&quot;</span><span class="p">,</span>
    <span class="n">check_timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
    <span class="n">nodebalancer_id</span><span class="o">=</span><span class="n">foobar</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">stickiness</span><span class="o">=</span><span class="s2">&quot;http_cookie&quot;</span><span class="p">)</span>
<span class="n">foonode</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">)]:</span>
    <span class="n">foonode</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">linode</span><span class="o">.</span><span class="n">NodeBalancerNode</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;foonode-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">address</span><span class="o">=</span><span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">private_ip_address</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">web</span><span class="p">][</span><span class="nb">range</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">]]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">private_ip_addresses</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">private_ip_addresses</span><span class="si">}</span><span class="s2">:80&quot;</span><span class="p">),</span>
        <span class="n">config_id</span><span class="o">=</span><span class="n">foofig</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">label</span><span class="o">=</span><span class="s2">&quot;mynodebalancernode&quot;</span><span class="p">,</span>
        <span class="n">nodebalancer_id</span><span class="o">=</span><span class="n">foobar</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">weight</span><span class="o">=</span><span class="mi">50</span><span class="p">))</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - The current status of this node, based on the configured checks of its NodeBalancer Config. (unknown, UP, DOWN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">config_id</span></code> - The ID of the NodeBalancerConfig this NodeBalancerNode is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodebalancer_id</span></code> - The ID of the NodeBalancer this NodeBalancerNode is attached to.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private IP Address where this backend can be reached. This must be a private IP address.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the NodeBalancerConfig to access.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode NodeBalancer Node. This is for display purposes only.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode this NodeBalancer should use when sending traffic to this backend. If set to <code class="docutils literal notranslate"><span class="pre">accept</span></code> this backend is accepting traffic. If set to <code class="docutils literal notranslate"><span class="pre">reject</span></code> this backend will not receive traffic. If set to <code class="docutils literal notranslate"><span class="pre">drain</span></code> this backend will not receive new traffic, but connections already pinned to it will continue to be routed to it</p></li>
<li><p><strong>nodebalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the NodeBalancer to access.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Used when picking a backend to serve a request and is not pinned to a single backend yet. Nodes with a higher weight will receive more traffic. (1-255).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodebalancer_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.node_balancer_node.NodeBalancerNode<a class="headerlink" href="#pulumi_linode.NodeBalancerNode.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeBalancerNode resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private IP Address where this backend can be reached. This must be a private IP address.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the NodeBalancerConfig to access.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode NodeBalancer Node. This is for display purposes only.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode this NodeBalancer should use when sending traffic to this backend. If set to <code class="docutils literal notranslate"><span class="pre">accept</span></code> this backend is accepting traffic. If set to <code class="docutils literal notranslate"><span class="pre">reject</span></code> this backend will not receive traffic. If set to <code class="docutils literal notranslate"><span class="pre">drain</span></code> this backend will not receive new traffic, but connections already pinned to it will continue to be routed to it</p></li>
<li><p><strong>nodebalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the NodeBalancer to access.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current status of this node, based on the configured checks of its NodeBalancer Config. (unknown, UP, DOWN)</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Used when picking a backend to serve a request and is not pinned to a single backend yet. Nodes with a higher weight will receive more traffic. (1-255).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.address">
<em class="property">property </em><code class="sig-name descname">address</code><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP Address where this backend can be reached. This must be a private IP address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.config_id">
<em class="property">property </em><code class="sig-name descname">config_id</code><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancerConfig to access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode NodeBalancer Node. This is for display purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.mode">
<em class="property">property </em><code class="sig-name descname">mode</code><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode this NodeBalancer should use when sending traffic to this backend. If set to <code class="docutils literal notranslate"><span class="pre">accept</span></code> this backend is accepting traffic. If set to <code class="docutils literal notranslate"><span class="pre">reject</span></code> this backend will not receive traffic. If set to <code class="docutils literal notranslate"><span class="pre">drain</span></code> this backend will not receive new traffic, but connections already pinned to it will continue to be routed to it</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.nodebalancer_id">
<em class="property">property </em><code class="sig-name descname">nodebalancer_id</code><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.nodebalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancer to access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of this node, based on the configured checks of its NodeBalancer Config. (unknown, UP, DOWN)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.weight">
<em class="property">property </em><code class="sig-name descname">weight</code><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Used when picking a backend to serve a request and is not pinned to a single backend yet. Nodes with a higher weight will receive more traffic. (1-255).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancerNode.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.ObjectStorageBucket">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">ObjectStorageBucket</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert</span><span class="p">:</span> <span class="n">Union[ObjectStorageBucketCertArgs, Mapping[str, Any], Awaitable[Union[ObjectStorageBucketCertArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Object Storage Bucket resource. This can be used to create, modify, and delete Linodes Object Storage Buckets.</p>
<p>The following example shows how one might use this resource to create an Object Storage Bucket.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">primary</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_object_storage_cluster</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">)</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">ObjectStorageBucket</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">cluster</span><span class="o">=</span><span class="n">primary</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;</span><span class="si">%s</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster of the Linode Object Storage Bucket.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode Object Storage Bucket.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.ObjectStorageBucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert</span><span class="p">:</span> <span class="n">Union[ObjectStorageBucketCertArgs, Mapping[str, Any], Awaitable[Union[ObjectStorageBucketCertArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.object_storage_bucket.ObjectStorageBucket<a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ObjectStorageBucket resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster of the Linode Object Storage Bucket.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode Object Storage Bucket.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageBucket.cluster">
<em class="property">property </em><code class="sig-name descname">cluster</code><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster of the Linode Object Storage Bucket.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageBucket.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode Object Storage Bucket.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageBucket.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.ObjectStorageBucket.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.ObjectStorageKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">ObjectStorageKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Object Storage Key resource. This can be used to create, modify, and delete Linodes Object Storage Keys.</p>
<p>The following example shows how one might use this resource to create an Object Storage Key.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">ObjectStorageKey</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;image-access&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> - This keypair’s access key. This is not secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_key</span></code> - This keypair’s secret key.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label given to this key. For display purposes only.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.ObjectStorageKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.object_storage_key.ObjectStorageKey<a class="headerlink" href="#pulumi_linode.ObjectStorageKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ObjectStorageKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This keypair’s access key. This is not secret.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label given to this key. For display purposes only.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This keypair’s secret key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageKey.access_key">
<em class="property">property </em><code class="sig-name descname">access_key</code><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>This keypair’s access key. This is not secret.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageKey.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label given to this key. For display purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageKey.secret_key">
<em class="property">property </em><code class="sig-name descname">secret_key</code><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>This keypair’s secret key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.ObjectStorageKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.ObjectStorageObject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">ObjectStorageObject</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_control</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_base64</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_disposition</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_encoding</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_language</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_destroy</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website_redirect</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageObject" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Object Storage Object resource. This can be used to create, modify, and delete Linodes Object Storage Objects for Buckets.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="nb">object</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">ObjectStorageObject</span><span class="p">(</span><span class="s2">&quot;object&quot;</span><span class="p">,</span>
    <span class="n">bucket</span><span class="o">=</span><span class="s2">&quot;my-bucket&quot;</span><span class="p">,</span>
    <span class="n">cluster</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;my-object&quot;</span><span class="p">,</span>
    <span class="n">secret_key</span><span class="o">=</span><span class="n">linode_object_storage_key</span><span class="p">[</span><span class="s2">&quot;my_key&quot;</span><span class="p">][</span><span class="s2">&quot;secret_key&quot;</span><span class="p">],</span>
    <span class="n">access_key</span><span class="o">=</span><span class="n">linode_object_storage_key</span><span class="p">[</span><span class="s2">&quot;my_key&quot;</span><span class="p">][</span><span class="s2">&quot;access_key&quot;</span><span class="p">],</span>
    <span class="n">content</span><span class="o">=</span><span class="s2">&quot;This is the content of the Object...&quot;</span><span class="p">,</span>
    <span class="n">content_type</span><span class="o">=</span><span class="s2">&quot;text/plain&quot;</span><span class="p">,</span>
    <span class="n">content_language</span><span class="o">=</span><span class="s2">&quot;en&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access key to authenticate with.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The canned ACL to apply. Can be either <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public-read</span></code> (defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>).</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put the object in.</p></li>
<li><p><strong>cache_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies caching behavior along the request/reply chain Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">w3c cache_control</a> for further details.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster the bucket is in.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p></li>
<li><p><strong>content_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the <code class="docutils literal notranslate"><span class="pre">gzipbase64</span></code> function with small text strings. For larger objects, use <code class="docutils literal notranslate"><span class="pre">source</span></code> to stream the content from a disk file.</p></li>
<li><p><strong>content_disposition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies presentational information for the object. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1">w3c content_disposition</a> for further information.</p></li>
<li><p><strong>content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">w3c content encoding</a> for further information.</p></li>
<li><p><strong>content_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The language the content is in e.g. en-US or en-GB.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow the object to be deleted regardless of any legal hold or object lock (defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – They name of the object once it is in the bucket.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of keys/values to provision metadata.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret key to authenitcate with.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to a file that will be read and uploaded as raw bytes for the object content. The path must either be relative to the root module or absolute.</p></li>
<li><p><strong>website_redirect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a target URL for website redirect.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_control</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_base64</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_disposition</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_encoding</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_language</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_destroy</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website_redirect</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.object_storage_object.ObjectStorageObject<a class="headerlink" href="#pulumi_linode.ObjectStorageObject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ObjectStorageObject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access key to authenticate with.</p></li>
<li><p><strong>acl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The canned ACL to apply. Can be either <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public-read</span></code> (defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>).</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bucket to put the object in.</p></li>
<li><p><strong>cache_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies caching behavior along the request/reply chain Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">w3c cache_control</a> for further details.</p>
</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster the bucket is in.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p></li>
<li><p><strong>content_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the <code class="docutils literal notranslate"><span class="pre">gzipbase64</span></code> function with small text strings. For larger objects, use <code class="docutils literal notranslate"><span class="pre">source</span></code> to stream the content from a disk file.</p></li>
<li><p><strong>content_disposition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies presentational information for the object. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1">w3c content_disposition</a> for further information.</p>
</p></li>
<li><p><strong>content_encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">w3c content encoding</a> for further information.</p>
</p></li>
<li><p><strong>content_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The language the content is in e.g. en-US or en-GB.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow the object to be deleted regardless of any legal hold or object lock (defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – They name of the object once it is in the bucket.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of keys/values to provision metadata.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret key to authenitcate with.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to a file that will be read and uploaded as raw bytes for the object content. The path must either be relative to the root module or absolute.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique version ID value for the object.</p></li>
<li><p><strong>website_redirect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a target URL for website redirect.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.access_key">
<em class="property">property </em><code class="sig-name descname">access_key</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The access key to authenticate with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.acl">
<em class="property">property </em><code class="sig-name descname">acl</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.acl" title="Permalink to this definition">¶</a></dt>
<dd><p>The canned ACL to apply. Can be either <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public-read</span></code> (defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.bucket">
<em class="property">property </em><code class="sig-name descname">bucket</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bucket to put the object in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.cache_control">
<em class="property">property </em><code class="sig-name descname">cache_control</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.cache_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies caching behavior along the request/reply chain Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">w3c cache_control</a> for further details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.cluster">
<em class="property">property </em><code class="sig-name descname">cluster</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster the bucket is in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.content">
<em class="property">property </em><code class="sig-name descname">content</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.content" title="Permalink to this definition">¶</a></dt>
<dd><p>Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.content_base64">
<em class="property">property </em><code class="sig-name descname">content_base64</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.content_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the <code class="docutils literal notranslate"><span class="pre">gzipbase64</span></code> function with small text strings. For larger objects, use <code class="docutils literal notranslate"><span class="pre">source</span></code> to stream the content from a disk file.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.content_disposition">
<em class="property">property </em><code class="sig-name descname">content_disposition</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.content_disposition" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies presentational information for the object. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1">w3c content_disposition</a> for further information.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.content_encoding">
<em class="property">property </em><code class="sig-name descname">content_encoding</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.content_encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read <a class="reference external" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11">w3c content encoding</a> for further information.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.content_language">
<em class="property">property </em><code class="sig-name descname">content_language</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.content_language" title="Permalink to this definition">¶</a></dt>
<dd><p>The language the content is in e.g. en-US or en-GB.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.content_type">
<em class="property">property </em><code class="sig-name descname">content_type</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.force_destroy">
<em class="property">property </em><code class="sig-name descname">force_destroy</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow the object to be deleted regardless of any legal hold or object lock (defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.key" title="Permalink to this definition">¶</a></dt>
<dd><p>They name of the object once it is in the bucket.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.metadata">
<em class="property">property </em><code class="sig-name descname">metadata</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of keys/values to provision metadata.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.secret_key">
<em class="property">property </em><code class="sig-name descname">secret_key</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret key to authenitcate with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.source">
<em class="property">property </em><code class="sig-name descname">source</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.source" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to a file that will be read and uploaded as raw bytes for the object content. The path must either be relative to the root module or absolute.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.version_id">
<em class="property">property </em><code class="sig-name descname">version_id</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique version ID value for the object.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.website_redirect">
<em class="property">property </em><code class="sig-name descname">website_redirect</code><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.website_redirect" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a target URL for website redirect.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageObject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.ObjectStorageObject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageObject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ua_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the linode package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An HTTP User-Agent Prefix to prepend in API requests.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token that allows you access to your Linode account</p></li>
<li><p><strong>ua_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An HTTP User-Agent Prefix to prepend in API requests.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP(S) API address of the Linode API to use.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.Rdns">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Rdns</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rdns</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode RDNS resource.  This can be used to create and modify RDNS records.</p>
<p>Linode RDNS names must have a matching address value in an A or AAAA record.  This A or AAAA name must be resolvable at the time the RDNS resource is being associated.</p>
<p>For more information, see the <a class="reference external" href="https://developers.linode.com/api/v4/networking-ips-address/#put">Linode APIv4 docs</a> and the <a class="reference external" href="https://www.linode.com/docs/networking/dns/configure-your-linode-for-reverse-dns-classic-manager/">Configure your Linode for Reverse DNS</a> guide.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Public IPv4 or IPv6 address that will receive the <code class="docutils literal notranslate"><span class="pre">PTR</span></code> record.  A matching <code class="docutils literal notranslate"><span class="pre">A</span></code> or <code class="docutils literal notranslate"><span class="pre">AAAA</span></code> record must exist.</p></li>
<li><p><strong>rdns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the RDNS address.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.Rdns.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rdns</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.rdns.Rdns<a class="headerlink" href="#pulumi_linode.Rdns.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rdns resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Public IPv4 or IPv6 address that will receive the <code class="docutils literal notranslate"><span class="pre">PTR</span></code> record.  A matching <code class="docutils literal notranslate"><span class="pre">A</span></code> or <code class="docutils literal notranslate"><span class="pre">AAAA</span></code> record must exist.</p></li>
<li><p><strong>rdns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the RDNS address.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Rdns.address">
<em class="property">property </em><code class="sig-name descname">address</code><a class="headerlink" href="#pulumi_linode.Rdns.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Public IPv4 or IPv6 address that will receive the <code class="docutils literal notranslate"><span class="pre">PTR</span></code> record.  A matching <code class="docutils literal notranslate"><span class="pre">A</span></code> or <code class="docutils literal notranslate"><span class="pre">AAAA</span></code> record must exist.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Rdns.rdns">
<em class="property">property </em><code class="sig-name descname">rdns</code><a class="headerlink" href="#pulumi_linode.Rdns.rdns" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the RDNS address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Rdns.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Rdns.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.SshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode SSH Key resource.  This can be used to create, modify, and delete Linodes SSH Keys.  Managed SSH Keys allow instances to be created with a list of Linode usernames, whose SSH keys will be automatically applied to the root account’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file.
For more information, see the <a class="reference external" href="https://developers.linode.com/api/v4#operation/getSSHKeys">Linode APIv4 docs</a>.</p>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">created</span></code> - The date this SSH Key was created.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the SSH Key.</p></li>
<li><p><strong>ssh_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.ssh_key.SshKey<a class="headerlink" href="#pulumi_linode.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this key was added.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the SSH Key.</p></li>
<li><p><strong>ssh_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.SshKey.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_linode.SshKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this key was added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.SshKey.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.SshKey.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A label for the SSH Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.SshKey.ssh_key">
<em class="property">property </em><code class="sig-name descname">ssh_key</code><a class="headerlink" href="#pulumi_linode.SshKey.ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.SshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.SshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.StackScript">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">StackScript</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rev_note</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_fields</span><span class="p">:</span> <span class="n">Union[List[Union[StackScriptUserDefinedFieldArgs, Mapping[str, Any], Awaitable[Union[StackScriptUserDefinedFieldArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[StackScriptUserDefinedFieldArgs, Mapping[str, Any], Awaitable[Union[StackScriptUserDefinedFieldArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode StackScript resource.  This can be used to create, modify, and delete Linode StackScripts.  StackScripts are private or public managed scripts which run within an instance during startup.  StackScripts can include variables whose values are specified when the Instance is created.</p>
<p>For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/stackscripts/">Automate Deployment with StackScripts</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#tag/StackScripts">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure a StackScript attached to a Linode Instance.  As shown below, StackScripts must begin with a shebang (<code class="docutils literal notranslate"><span class="pre">#!/</span></code>).  The <code class="docutils literal notranslate"><span class="pre">&lt;UDF</span> <span class="pre">...&gt;</span></code> element provided in the Bash comment block defines a variable whose value is provided when creating the Instance (or disk) using the <code class="docutils literal notranslate"><span class="pre">stackscript_data</span></code> field.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo_stack_script</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">StackScript</span><span class="p">(</span><span class="s2">&quot;fooStackScript&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Installs a Package&quot;</span><span class="p">,</span>
    <span class="n">images</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;linode/ubuntu18.04&quot;</span><span class="p">,</span>
        <span class="s2">&quot;linode/ubuntu16.04lts&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">rev_note</span><span class="o">=</span><span class="s2">&quot;initial version&quot;</span><span class="p">,</span>
    <span class="n">script</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;#!/bin/bash</span>
<span class="s2"># &lt;UDF name=&quot;package&quot; label=&quot;System Package to Install&quot; example=&quot;nginx&quot; default=&quot;&quot;&gt;</span>
<span class="s2">apt-get -q update &amp;&amp; apt-get -q -y install $PACKAGE</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">foo_instance</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;fooInstance&quot;</span><span class="p">,</span>
    <span class="n">authorized_keys</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;...&quot;</span><span class="p">],</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;linode/ubuntu18.04&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">,</span>
    <span class="n">root_pass</span><span class="o">=</span><span class="s2">&quot;...&quot;</span><span class="p">,</span>
    <span class="n">stackscript_data</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;package&quot;</span><span class="p">:</span> <span class="s2">&quot;nginx&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">stackscript_id</span><span class="o">=</span><span class="n">linode_stackscript</span><span class="p">[</span><span class="s2">&quot;install-nginx&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-nanode-1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployments_active</span></code> - Count of currently active, deployed Linodes created from this StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_gravatar_id</span></code> - The Gravatar ID for the User who created the StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deployments_total</span></code> - The total number of times this StackScript has been deployed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> - The User who created the StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created</span></code> - The date this StackScript was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated</span></code> - The date this StackScript was updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_defined_fields</span></code> - This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> - A human-readable label for the field that will serve as the input prompt for entering the value during deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - The name of the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">example</span></code> - An example value for the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">one_of</span></code> - A list of acceptable single values for the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">many_of</span></code> - A list of acceptable values for the field in any quantity, combination or order.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> - The default value. If not specified, this value will be used.</p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the StackScript.</p></li>
<li><p><strong>images</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em></p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The StackScript’s label is for display purposes only.</p></li>
<li><p><strong>rev_note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field allows you to add notes for the set of revisions made to this StackScript.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script to execute when provisioning a new Linode with this StackScript.</p></li>
<li><p><strong>user_defined_fields</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'StackScriptUserDefinedFieldArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized
parameters during deployment.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.StackScript.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployments_active</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployments_total</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rev_note</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_fields</span><span class="p">:</span> <span class="n">Union[List[Union[StackScriptUserDefinedFieldArgs, Mapping[str, Any], Awaitable[Union[StackScriptUserDefinedFieldArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[StackScriptUserDefinedFieldArgs, Mapping[str, Any], Awaitable[Union[StackScriptUserDefinedFieldArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_gravatar_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.stack_script.StackScript<a class="headerlink" href="#pulumi_linode.StackScript.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StackScript resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this StackScript was created.</p></li>
<li><p><strong>deployments_active</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Count of currently active, deployed Linodes created from this StackScript.</p></li>
<li><p><strong>deployments_total</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The total number of times this StackScript has been deployed.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the StackScript.</p></li>
<li><p><strong>images</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em></p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The StackScript’s label is for display purposes only.</p></li>
<li><p><strong>rev_note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field allows you to add notes for the set of revisions made to this StackScript.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script to execute when provisioning a new Linode with this StackScript.</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this StackScript was updated.</p></li>
<li><p><strong>user_defined_fields</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'StackScriptUserDefinedFieldArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized
parameters during deployment.</p></li>
<li><p><strong>user_gravatar_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Gravatar ID for the User who created the StackScript.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User who created the StackScript.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_linode.StackScript.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this StackScript was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.deployments_active">
<em class="property">property </em><code class="sig-name descname">deployments_active</code><a class="headerlink" href="#pulumi_linode.StackScript.deployments_active" title="Permalink to this definition">¶</a></dt>
<dd><p>Count of currently active, deployed Linodes created from this StackScript.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.deployments_total">
<em class="property">property </em><code class="sig-name descname">deployments_total</code><a class="headerlink" href="#pulumi_linode.StackScript.deployments_total" title="Permalink to this definition">¶</a></dt>
<dd><p>The total number of times this StackScript has been deployed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_linode.StackScript.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the StackScript.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.images">
<em class="property">property </em><code class="sig-name descname">images</code><a class="headerlink" href="#pulumi_linode.StackScript.images" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.is_public">
<em class="property">property </em><code class="sig-name descname">is_public</code><a class="headerlink" href="#pulumi_linode.StackScript.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.StackScript.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The StackScript’s label is for display purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.rev_note">
<em class="property">property </em><code class="sig-name descname">rev_note</code><a class="headerlink" href="#pulumi_linode.StackScript.rev_note" title="Permalink to this definition">¶</a></dt>
<dd><p>This field allows you to add notes for the set of revisions made to this StackScript.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.script">
<em class="property">property </em><code class="sig-name descname">script</code><a class="headerlink" href="#pulumi_linode.StackScript.script" title="Permalink to this definition">¶</a></dt>
<dd><p>The script to execute when provisioning a new Linode with this StackScript.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_linode.StackScript.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this StackScript was updated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.user_defined_fields">
<em class="property">property </em><code class="sig-name descname">user_defined_fields</code><a class="headerlink" href="#pulumi_linode.StackScript.user_defined_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized
parameters during deployment.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.user_gravatar_id">
<em class="property">property </em><code class="sig-name descname">user_gravatar_id</code><a class="headerlink" href="#pulumi_linode.StackScript.user_gravatar_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Gravatar ID for the User who created the StackScript.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_linode.StackScript.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The User who created the StackScript.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.StackScript.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.Token">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Token</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Token resource.  This can be used to create, modify, and delete Linode API Personal Access Tokens.  Personal Access Tokens proxy user credentials for Linode API access.  This is necessary for tools, to interact with Linode services on a user’s behalf.</p>
<p>It is common for the provider itself to be configured with broadly scoped Personal Access Tokens.  Provisioning scripts or tools configured within a Linode Instance should follow the principle of least privilege to afford only the required roles for tools to perform their necessary tasks.  The <code class="docutils literal notranslate"><span class="pre">Token</span></code> resource allows for the management of Personal Access Tokens with scopes mirroring or narrowing the scope of the parent token.</p>
<p>For more information, see the <a class="reference external" href="https://developers.linode.com/api/v4#operation/getTokens">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure a token for use in another tool that needs access to Linode resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo_token</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Token</span><span class="p">(</span><span class="s2">&quot;fooToken&quot;</span><span class="p">,</span>
    <span class="n">expiry</span><span class="o">=</span><span class="s2">&quot;2100-01-02T03:04:05Z&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;token&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="s2">&quot;linodes:read_only&quot;</span><span class="p">)</span>
<span class="n">foo_instance</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;fooInstance&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> - The token used to access the API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created</span></code> - The date this Token was created.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the Token.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id28"><span class="problematic" id="id29">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.Token.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.token.Token<a class="headerlink" href="#pulumi_linode.Token.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Token resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time this token was created.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the Token.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id30"><span class="problematic" id="id31">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token used to access the API.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Token.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_linode.Token.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time this token was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Token.expiry">
<em class="property">property </em><code class="sig-name descname">expiry</code><a class="headerlink" href="#pulumi_linode.Token.expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Token.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.Token.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A label for the Token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Token.scopes">
<em class="property">property </em><code class="sig-name descname">scopes</code><a class="headerlink" href="#pulumi_linode.Token.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id32"><span class="problematic" id="id33">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Token.token">
<em class="property">property </em><code class="sig-name descname">token</code><a class="headerlink" href="#pulumi_linode.Token.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token used to access the API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Token.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Token.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_linode.Volume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Volume resource.  This can be used to create, modify, and delete Linodes Block Storage Volumes.  Block Storage Volumes are removable storage disks that persist outside the life-cycle of Linode Instances. These volumes can be attached to and detached from Linode instances throughout a region.</p>
<p>For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/block-storage/how-to-use-block-storage-with-your-linode/">How to Use Block Storage with Your Linode</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createVolume">Linode APIv4 docs</a>.</p>
<p>The following example shows how one might use this resource to configure a Block Storage Volume attached to a Linode Instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foobaz</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;foobaz&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-west&quot;</span><span class="p">,</span>
    <span class="n">root_pass</span><span class="o">=</span><span class="s2">&quot;3X4mp13&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foobaz&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-nanode-1&quot;</span><span class="p">)</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;foo-volume&quot;</span><span class="p">,</span>
    <span class="n">linode_id</span><span class="o">=</span><span class="n">foobaz</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="n">foobaz</span><span class="o">.</span><span class="n">region</span><span class="p">)</span>
</pre></div>
</div>
<p>Volumes can also be attached using the Linode Instance config device map.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">configs</span><span class="o">=</span><span class="p">[</span><span class="n">linode</span><span class="o">.</span><span class="n">InstanceConfigArgs</span><span class="p">(</span>
        <span class="n">devices</span><span class="o">=</span><span class="n">linode</span><span class="o">.</span><span class="n">InstanceConfigDevicesArgs</span><span class="p">(</span>
            <span class="n">sda</span><span class="o">=</span><span class="n">linode</span><span class="o">.</span><span class="n">InstanceConfigDevicesSdaArgs</span><span class="p">(</span>
                <span class="n">volume_id</span><span class="o">=</span><span class="mi">123</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">kernel</span><span class="o">=</span><span class="s2">&quot;linode/latest-64bit&quot;</span><span class="p">,</span>
        <span class="n">label</span><span class="o">=</span><span class="s2">&quot;boot-existing-volume&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-nanode-1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - The label of the Linode Volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filesystem_path</span></code> - The full filesystem path for the Volume based on the Volume’s label. The path is “/dev/disk/by-id/scsi-0Linode<em>Volume</em>” + the Volume label</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode Volume</p></li>
<li><p><strong>linode_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of a Linode Instance where the Volume should be attached.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this volume will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Volume.</em>.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the Volume in GB.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_linode.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filesystem_path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.volume.Volume<a class="headerlink" href="#pulumi_linode.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>filesystem_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full filesystem path for the Volume based on the Volume’s label. Path is /dev/disk/by-id/scsi-0Linode<em>Volume</em> +
Volume label.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode Volume</p></li>
<li><p><strong>linode_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of a Linode Instance where the Volume should be attached.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this volume will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Volume.</em>.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the Volume in GB.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the volume, indicating the current readiness state.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.filesystem_path">
<em class="property">property </em><code class="sig-name descname">filesystem_path</code><a class="headerlink" href="#pulumi_linode.Volume.filesystem_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The full filesystem path for the Volume based on the Volume’s label. Path is /dev/disk/by-id/scsi-0Linode<em>Volume</em> +
Volume label.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_linode.Volume.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode Volume</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.linode_id">
<em class="property">property </em><code class="sig-name descname">linode_id</code><a class="headerlink" href="#pulumi_linode.Volume.linode_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Linode Instance where the Volume should be attached.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_linode.Volume.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where this volume will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Volume.</em>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_linode.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the Volume in GB.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_linode.Volume.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the volume, indicating the current readiness state.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_linode.Volume.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Volume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.get_account">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_account.AwaitableGetAccountResult<a class="headerlink" href="#pulumi_linode.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode account.</p>
<p>This data source should not be used in conjuction with the <code class="docutils literal notranslate"><span class="pre">LINODE_DEBUG</span></code> option.  See the <a class="reference external" href="https://www.terraform.io/providers/linode/linode/latest/docs#debugging">debugging notes</a> for more details.</p>
<p>The following example shows how one might use this data source to access account details.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">account</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_account</span><span class="p">()</span>
</pre></div>
</div>
<p>The Linode Account resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> - The email address for this Account, for account management communications, and may be used for other communications as configured.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">first_name</span></code> - The first name of the person associated with this Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last_name</span></code> - The last name of the person associated with this Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">company</span></code> - The company name associated with this Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">address_1</span></code> - First line of this Account’s billing address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">address_2</span></code> - Second line of this Account’s billing address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">phone</span></code> - The phone number associated with this Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">city</span></code> - The city for this Account’s billing address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> - If billing address is in the United States, this is the State portion of the Account’s billing address. If the address is outside the US, this is the Province associated with the Account’s billing address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> - The two-letter country code of this Account’s billing address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zip</span></code> - The zip code of this Account’s billing address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">balance</span></code> - This Account’s balance, in US dollars.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_domain">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_domain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_domain.AwaitableGetDomainResult<a class="headerlink" href="#pulumi_linode.get_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode domain.</p>
<p>The following example shows how one might use this data source to access information about a Linode domain.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_domain</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;1234567&quot;</span><span class="p">)</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_domain</span><span class="p">(</span><span class="n">domain</span><span class="o">=</span><span class="s2">&quot;bar.example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The Linode Domain resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The unique ID of this Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> - The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> - The group this Domain belongs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - Used to control whether this Domain is currently being rendered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - A description for this Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_ips</span></code> - The IP addresses representing the master DNS for this Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">axfr_ips</span></code> - The list of IPs that may perform a zone transfer for this Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl_sec</span></code> - ‘Time to Live’-the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retry_sec</span></code> - The interval, in seconds, at which a failed refresh should be retried.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expire_sec</span></code> - The amount of time in seconds that may pass before this Domain is no longer authoritative.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">refresh_sec</span></code> - The amount of time in seconds before this Domain should be refreshed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">soa_email</span></code> - Start of Authority email address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> - An array of tags applied to this object.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>str</em>) – The unique domain name of the Domain record to query.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique numeric ID of the Domain record to query.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_domain_record">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_domain_record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_domain_record.AwaitableGetDomainRecordResult<a class="headerlink" href="#pulumi_linode.get_domain_record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Domain Record.</p>
<p>The following example shows how one might use this data source to access information about a Linode Domain Record.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">my_record</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_domain_record</span><span class="p">(</span><span class="n">domain_id</span><span class="o">=</span><span class="mi">3150401</span><span class="p">,</span>
    <span class="nb">id</span><span class="o">=</span><span class="mi">14950401</span><span class="p">)</span>
<span class="n">my_www_record</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_domain_record</span><span class="p">(</span><span class="n">domain_id</span><span class="o">=</span><span class="mi">3150401</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;www&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The Linode Volume resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The unique ID of the Domain Record.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - The name of the Record.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_id</span></code> - The associated domain’s unique ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - The type of Record this is in the DNS system.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl_sec</span></code> - The amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> - The target for this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> - The priority of the target host. Lower values are preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> - The relative weight of this Record. Higher values are preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> - The port this Record points to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> - The protocol this Record’s service communicates with. Only valid for SRV records.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> - The service this Record identified. Only valid for SRV records.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> - The tag portion of a CAA record.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_id</strong> (<em>float</em>) – The associated domain’s unique ID.</p></li>
<li><p><strong>id</strong> (<em>float</em>) – The unique ID of the Domain Record.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Record.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_image">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_image.AwaitableGetImageResult<a class="headerlink" href="#pulumi_linode.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode image</p>
<p>The following example shows how one might use this data source to access information about a Linode image.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">k8_master</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_image</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;linode/debian8&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The Linode Image resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> - A short description of the Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created</span></code> - When this Image was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created_by</span></code> - The name of the User who created this Image, or “linode” for official Images.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deprecated</span></code> - Whether or not this Image is deprecated. Will only be true for deprecated public Images.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - A detailed description of this Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_public</span></code> - True if the Image is public.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> - The minimum size this Image needs to deploy. Size is in MB. example: 2500</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - How the Image was created. Manual Images can be created at any time. image”Automatic” Images are created automatically from a deleted Linode.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vendor</span></code> - The upstream distribution vendor. <code class="docutils literal notranslate"><span class="pre">None</span></code> for private Images.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>str</em>) – The unique ID of this Image.  The ID of private images begin with <code class="docutils literal notranslate"><span class="pre">private/</span></code> followed by the numeric identifier of the private image, for example <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_instance_type">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_instance_type</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_instance_type.AwaitableGetInstanceTypeResult<a class="headerlink" href="#pulumi_linode.get_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode instance type</p>
<p>The following example shows how one might use this data source to access information about a Linode Instance type.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_instance_type</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;g6-standard-2&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The Linode Instance Type resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The ID representing the Linode Type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> - The Linode Type’s label is for display purposes only</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">class</span></code> - The class of the Linode Type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk</span></code> - The Disk size, in MB, of the Linode Type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">price.0.hourly</span></code> -  Cost (in US dollars) per hour.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">price.0.monthly</span></code> - Cost (in US dollars) per month.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">addons.0.backups.0.price.0.hourly</span></code> - The cost (in US dollars) per hour to add Backups service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">addons.0.backups.0.price.0.monthly</span></code> - The cost (in US dollars) per month to add Backups service.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>str</em>) – Label used to identify instance type</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_networking_ip">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_networking_ip</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_networking_ip.AwaitableGetNetworkingIpResult<a class="headerlink" href="#pulumi_linode.get_networking_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Networking IP Address</p>
<p>The following example shows how one might use this data source to access information about a Linode Networking IP Address.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">ns1_linode_com</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_networking_ip</span><span class="p">(</span><span class="n">address</span><span class="o">=</span><span class="s2">&quot;162.159.27.72&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The Linode Network IP Address resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> - The IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gateway</span></code> - The default gateway for this address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_mask</span></code> - The mask that separates host bits from network bits for this address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> - The number of bits set in the subnet mask.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - The type of address this is (ipv4, ipv6, ipv6/pool, ipv6/range).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public</span></code> - Whether this is a public or private IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdns</span></code> - The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linode_id</span></code> - The ID of the Linode this address currently belongs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> - The Region this IP address resides in.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>address</strong> (<em>str</em>) – The IP Address to access.  The address must be associated with the account and a resource that the user has access to view.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_object_storage_cluster">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_object_storage_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_site_domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_object_storage_cluster.AwaitableGetObjectStorageClusterResult<a class="headerlink" href="#pulumi_linode.get_object_storage_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Object Storage Cluster</p>
<p>The following example shows how one might use this data source to access information about a Linode Object Storage Cluster.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">primary</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_object_storage_cluster</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The Linode Object Storage Cluster resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> - The base URL for this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - This cluster’s status.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> - The region this cluster is located in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">static_site_domain</span></code> - The base URL for this cluster used when hosting static sites.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>str</em>) – The unique ID of this cluster.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_profile">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_profile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_profile.AwaitableGetProfileResult<a class="headerlink" href="#pulumi_linode.get_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode profile.</p>
<p>The following example shows how one might use this data source to access profile details.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">profile</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_profile</span><span class="p">()</span>
</pre></div>
</div>
<p>The Linode Profile resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> - The profile email address. This address will be used for communication with Linode as necessary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> - The profile’s preferred timezone. This is not used by the API, and is for the benefit of clients only. All times the API returns are in UTC.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_notifications</span></code> - If true, email notifications will be sent about account activity. If false, when false business-critical communications may still be sent through email.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> - The username for logging in to Linode services.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_whitelist_enabled</span></code> - If true, logins for the user will only be allowed from whitelisted IPs. This setting is currently deprecated, and cannot be enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lish_auth_method</span></code> - The methods of authentication allowed when connecting via Lish. ‘keys_only’ is the most secure with the intent to use Lish, and ‘disabled’ is recommended for users that will not use Lish at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code> - The list of SSH Keys authorized to use Lish for this user. This value is ignored if lish_auth_method is ‘disabled’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">two_factor_auth</span></code> - If true, logins from untrusted computers will require Two Factor Authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restricted</span></code> - If true, the user has restrictions on what can be accessed on the Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referrals</span></code> - Credit Card information associated with this Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referrals.0.total</span></code> - The number of users who have signed up with the referral code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referrals.0.credit</span></code> - The amount of account credit in US Dollars issued to the account through the referral program.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referrals.0.completed</span></code> - The number of completed signups with the referral code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referrals.0.pending</span></code> - The number of pending signups for the referral code. To receive credit the signups must be completed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referrals.0.code</span></code> - The Profile referral code.  If new accounts use this when signing up for Linode, referring account will receive credit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referrals.0.url</span></code> - The referral URL.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_region">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_region</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">country</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_region.AwaitableGetRegionResult<a class="headerlink" href="#pulumi_linode.get_region" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getRegion</span></code> provides details about a specific Linode region. See all regions <a class="reference external" href="https://api.linode.com/v4/regions">here</a>.</p>
<p>The following example shows how the resource might be used to obtain additional information about a Linode region.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">region</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_region</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>country</strong> (<em>str</em>) – The country the region resides in.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The code name of the region to select.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_ssh_key">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_ssh_key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_ssh_key.AwaitableGetSshKeyResult<a class="headerlink" href="#pulumi_linode.get_ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">SshKey</span></code> provides access to a specifically labeled SSH Key in the Profile of the User identified by the access token.</p>
<p>The following example shows how the resource might be used to obtain the name of the SSH Key configured on the Linode user profile.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_ssh_key</span><span class="p">(</span><span class="n">label</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>label</strong> (<em>str</em>) – The label of the SSH Key to select.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_stack_script">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_stack_script</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_fields</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetStackScriptUserDefinedFieldArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_stack_script.AwaitableGetStackScriptResult<a class="headerlink" href="#pulumi_linode.get_stack_script" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Linode StackScript.</p>
<p>The following example shows how one might use this data source to access information about a Linode StackScript.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">my_stackscript</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_stack_script</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="mi">355872</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> - The StackScript’s label is for display purposes only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> - The script to execute when provisioning a new Linode with this StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - A description for the StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rev_note</span></code> - This field allows you to add notes for the set of revisions made to this StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_public</span></code> - This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">images</span></code> - An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deployments_active</span></code> - Count of currently active, deployed Linodes created from this StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_gravatar_id</span></code> - The Gravatar ID for the User who created the StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deployments_total</span></code> - The total number of times this StackScript has been deployed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> - The User who created the StackScript.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created</span></code> - The date this StackScript was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated</span></code> - The date this StackScript was updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_defined_fields</span></code> - This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> - A human-readable label for the field that will serve as the input prompt for entering the value during deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - The name of the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">example</span></code> - An example value for the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">one_of</span></code> - A list of acceptable single values for the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">many_of</span></code> - A list of acceptable values for the field in any quantity, combination or order.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> - The default value. If not specified, this value will be used.</p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>float</em>) – The unique numeric ID of the StackScript to query.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_user">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_user.AwaitableGetUserResult<a class="headerlink" href="#pulumi_linode.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode user</p>
<p>The following example shows how one might use this data source to access information about a Linode user.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The Linode User resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ssh_keys</span></code> - A list of SSH Key labels added by this User. These are the keys that will be deployed if this User is included in the authorized_users field of a create Linode, rebuild Linode, or create Disk request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> - The email address for this User, for account management communications, and may be used for other communications as configured.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restricted</span></code> - If true, this User must be granted access to perform actions or access entities on this Account.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>username</strong> (<em>str</em>) – The unique username of this User.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_volume">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_linode.get_volume.AwaitableGetVolumeResult<a class="headerlink" href="#pulumi_linode.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Volume.</p>
<p>The following example shows how one might use this data source to access information about a Linode Volume.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_volume</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="mi">1234567</span><span class="p">)</span>
</pre></div>
</div>
<p>The Linode Volume resource exports the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The unique ID of this Volume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created</span></code> - When this Volume was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - The current status of the Volume. Can be one of “creating”, “active”, “resizing”, or “contact_support”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> - This Volume’s label is for display purposes only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> - An array of tags applied to this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> - The Volume’s size, in GiB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> - The datacenter in which this Volume is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated</span></code> - When this Volume was last updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">linode_id</span></code> - If a Volume is attached to a specific Linode, the ID of that Linode will be displayed here. If the Volume is unattached, this value will be null.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filesystem_path</span></code> - The full filesystem path for the Volume based on the Volume’s label. Path is /dev/disk/by-id/scsi-0LinodeVolume + Volume label.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>float</em>) – The unique numeric ID of the Volume record to query.</p>
</dd>
</dl>
</dd></dl>

</div>
