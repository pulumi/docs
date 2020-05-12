---
title: Package pulumi_linode
title_tag: Package pulumi_linode | Python SDK
linktitle: pulumi_linode
notitle: true
---

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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axfr_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expire_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">soa_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Domain resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] axfr_ips: The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.
:param pulumi.Input[str] description: A description for this Domain. This is for display purposes only.
:param pulumi.Input[str] domain: The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.
:param pulumi.Input[float] expire_sec: The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
:param pulumi.Input[str] group: The group this Domain belongs to. This is for display purposes only.
:param pulumi.Input[list] master_ips: The IP addresses representing the master DNS for this Domain.
:param pulumi.Input[float] refresh_sec: The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
:param pulumi.Input[float] retry_sec: The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
:param pulumi.Input[str] soa_email: Start of Authority email address. This is required for master Domains.
:param pulumi.Input[str] status: Used to control whether this Domain is currently being rendered (defaults to “active”).
:param pulumi.Input[list] tags: A list of tags applied to this object. Tags are for organizational purposes only.
:param pulumi.Input[float] ttl_sec: ‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
:param pulumi.Input[str] type: If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).</p>
<dl class="py attribute">
<dt id="pulumi_linode.Domain.axfr_ips">
<code class="sig-name descname">axfr_ips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.axfr_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this Domain. This is for display purposes only.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.expire_sec">
<code class="sig-name descname">expire_sec</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.expire_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.group">
<code class="sig-name descname">group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The group this Domain belongs to. This is for display purposes only.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.master_ips">
<code class="sig-name descname">master_ips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.master_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP addresses representing the master DNS for this Domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.refresh_sec">
<code class="sig-name descname">refresh_sec</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.refresh_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.retry_sec">
<code class="sig-name descname">retry_sec</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.retry_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.soa_email">
<code class="sig-name descname">soa_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.soa_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Start of Authority email address. This is required for master Domains.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to control whether this Domain is currently being rendered (defaults to “active”).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.ttl_sec">
<code class="sig-name descname">ttl_sec</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.ttl_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Domain.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.type" title="Permalink to this definition">¶</a></dt>
<dd><p>If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axfr_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expire_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">soa_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>axfr_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Domain. This is for display purposes only.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.</p></li>
<li><p><strong>expire_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group this Domain belongs to. This is for display purposes only.</p></li>
<li><p><strong>master_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP addresses representing the master DNS for this Domain.</p></li>
<li><p><strong>refresh_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>retry_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>soa_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Start of Authority email address. This is required for master Domains.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to control whether this Domain is currently being rendered (defaults to “active”).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
<li><p><strong>ttl_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">DomainRecord</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Domain Record resource.  This can be used to create, modify, and delete Linodes Domain Records.
For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/manager/dns-manager/">DNS Manager</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createDomainRecord">Linode APIv4 docs</a>.</p>
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
<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.domain_id">
<code class="sig-name descname">domain_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Domain to access.  <em>Changing ``domain_id`` forces the creation of a new Linode Domain Record.</em>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Record. Setting this is invalid for <code class="docutils literal notranslate"><span class="pre">SRV</span></code> records as it is generated by the API. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the subdomain being associated with an IP address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port this Record points to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the target host. Lower values are preferred.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol this Record’s service communicates with. Only valid for SRV records.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.record_type">
<code class="sig-name descname">record_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.record_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. <em>Changing ``record_type`` forces the creation of a new Linode Domain Record.</em>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The service this Record identified. Only valid for SRV records.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.tag">
<code class="sig-name descname">tag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag portion of a CAA record. It is invalid to set this on other record types.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.target">
<code class="sig-name descname">target</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The target for this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.ttl_sec">
<code class="sig-name descname">ttl_sec</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.ttl_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.DomainRecord.weight">
<code class="sig-name descname">weight</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>The relative weight of this Record. Higher values are preferred.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.DomainRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_linode.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address1</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">phone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zip</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="py attribute">
<dt id="pulumi_linode.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_linode.GetNetworkingIpResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetNetworkingIpResult.id" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_linode.GetProfileResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetRegionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetRegionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetRegionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegion.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_linode.GetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKey.</p>
<dl class="py attribute">
<dt id="pulumi_linode.GetSshKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetSshKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
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
<dl class="py attribute">
<dt id="pulumi_linode.GetUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Image resource.  This can be used to create, modify, and delete Linodes Images.  Linode Images are snapshots of a Linode Instance Disk which can then be used to provision more Linode Instances.  Images can be used across regions.</p>
<p>For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/disk-images/linode-images/">Linode’s documentation on Images</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createImage">Linode APIv4 docs</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-central&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;g6-nanode-1&quot;</span><span class="p">)</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">Image</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Image taken from foo&quot;</span><span class="p">,</span>
    <span class="n">disk_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">disks</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
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
<dl class="py attribute">
<dt id="pulumi_linode.Image.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.created" title="Permalink to this definition">¶</a></dt>
<dd><p>When this Image was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.created_by">
<code class="sig-name descname">created_by</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.created_by" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the User who created this Image.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.deprecated">
<code class="sig-name descname">deprecated</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.deprecated" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this Image is deprecated. Will only be True for deprecated public Images.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A detailed description of this Image.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.disk_id">
<code class="sig-name descname">disk_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Linode Disk that this Image will be created from.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.expiry">
<code class="sig-name descname">expiry</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>Only Images created automatically (from a deleted Linode; type=automatic) will expire.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.is_public">
<code class="sig-name descname">is_public</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>True if the Image is public.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the Image. Labels cannot contain special characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.linode_id">
<code class="sig-name descname">linode_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.linode_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Linode that this Image will be created from.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.size">
<code class="sig-name descname">size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size this Image needs to deploy. Size is in MB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.type" title="Permalink to this definition">¶</a></dt>
<dd><p>How the Image was created. ‘Manual’ Images can be created at any time. ‘Automatic’ images are created automatically from
a deleted Linode.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Image.vendor">
<code class="sig-name descname">vendor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.vendor" title="Permalink to this definition">¶</a></dt>
<dd><p>The upstream distribution vendor. Nil for private Images.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Image.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vendor</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Image resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alerts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boot_config_label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_pass</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stackscript_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stackscript_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">swap_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">watchdog_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Instance resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] authorized_keys: A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em>
:param pulumi.Input[list] authorized_users: A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em>
:param pulumi.Input[float] backup_id: A Backup ID from another Linode’s available backups. Your User must have read_write access to that Linode, the Backup must have a status of successful, and the Linode must be deployed to the same region as the Backup. See /linode/instances/{linodeId}/backups for a Linode’s available backups. This field and the image field are mutually exclusive. <em>This value can not be imported.</em> <em>Changing ``backup_id`` forces the creation of a new Linode Instance.</em>
:param pulumi.Input[bool] backups_enabled: If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.
:param pulumi.Input[str] boot_config_label: The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em>
:param pulumi.Input[list] configs: Configuration profiles define the VM settings and boot behavior of the Linode Instance.
:param pulumi.Input[str] group: The display group of the Linode instance.
:param pulumi.Input[str] image: An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. See all images <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em>
:param pulumi.Input[str] label: The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.
:param pulumi.Input[bool] private_ip: If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.
:param pulumi.Input[str] region: This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc. See all regions <a class="reference external" href="https://api.linode.com/v4/regions">here</a>. <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.
:param pulumi.Input[str] root_pass: The password that will be initialially assigned to the ‘root’ user account.
:param pulumi.Input[dict] stackscript_data: An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em>
:param pulumi.Input[float] stackscript_id: The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em>
:param pulumi.Input[float] swap_size: When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.
:param pulumi.Input[list] tags: A list of tags applied to this object. Tags are for organizational purposes only.
:param pulumi.Input[str] type: The Linode type defines the pricing, CPU, disk, and RAM specs of the instance. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc. See all types <a class="reference external" href="https://api.linode.com/v4/linode/types">here</a>.
:param pulumi.Input[bool] watchdog_enabled: The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.</p>
<p>The <strong>alerts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">io</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkOut</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transferQuota</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Arbitrary user comments about this <code class="docutils literal notranslate"><span class="pre">config</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">devices</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of <code class="docutils literal notranslate"><span class="pre">disk</span></code> or <code class="docutils literal notranslate"><span class="pre">volume</span></code> attachments for this <code class="docutils literal notranslate"><span class="pre">config</span></code>.  If the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code> omits a <code class="docutils literal notranslate"><span class="pre">devices</span></code> block, the Linode will not be booted.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sda</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - … <code class="docutils literal notranslate"><span class="pre">sdh</span></code> - (Optional) The SDA-SDH slots, represent the Linux block device nodes for the first 8 disks attached to the Linode.  Each device must be suplied sequentially.  The device can be either a Disk or a Volume identified by <code class="docutils literal notranslate"><span class="pre">disk_label</span></code> or <code class="docutils literal notranslate"><span class="pre">volume_id</span></code>. Only one disk identifier is permitted per slot. Devices mapped from <code class="docutils literal notranslate"><span class="pre">sde</span></code> through <code class="docutils literal notranslate"><span class="pre">sdh</span></code> are unavailable in <code class="docutils literal notranslate"><span class="pre">&quot;fullvirt&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">virt_mode</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sde</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdh</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">helpers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Helpers enabled when booting to this Linode Config.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">devtmpfsAutomount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">distro</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Controls the behavior of the Linode Config’s Distribution Helper setting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modulesDep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Creates a modules dependency file for the Kernel you run.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Controls the behavior of the Linode Config’s Network Helper setting, used to automatically configure additional IP addresses assigned to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updatedbDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Disables updatedb cron job to avoid disk thrashing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kernel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - A Kernel ID to boot a Linode with. Default is based on image choice. Examples are <code class="docutils literal notranslate"><span class="pre">linode/latest-64bit</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/grub2</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/direct-disk</span></code>, etc. See all kernels <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - - Defaults to the total RAM of the Linode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootDevice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - The root device to boot. The corresponding disk must be attached to a <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.  Example: <code class="docutils literal notranslate"><span class="pre">&quot;/dev/sda&quot;</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Defines the state of your Linode after booting. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Controls the virtualization mode. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;paravirt&quot;</span></code>.</p></li>
</ul>
<p>The <strong>disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorized_users</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filesystem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the disk in the Linode API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. See all images <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">root_pass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Disk in MB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackscript_data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackscript_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_linode.Instance.authorized_keys">
<code class="sig-name descname">authorized_keys</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.authorized_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.authorized_users">
<code class="sig-name descname">authorized_users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.authorized_users" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.backup_id">
<code class="sig-name descname">backup_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.backup_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A Backup ID from another Linode’s available backups. Your User must have read_write access to that Linode, the Backup must have a status of successful, and the Linode must be deployed to the same region as the Backup. See /linode/instances/{linodeId}/backups for a Linode’s available backups. This field and the image field are mutually exclusive. <em>This value can not be imported.</em> <em>Changing ``backup_id`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.backups">
<code class="sig-name descname">backups</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.backups" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about this Linode’s backups status.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedule</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.backups_enabled">
<code class="sig-name descname">backups_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.backups_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.boot_config_label">
<code class="sig-name descname">boot_config_label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.boot_config_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.configs">
<code class="sig-name descname">configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.configs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration profiles define the VM settings and boot behavior of the Linode Instance.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comments</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - - Arbitrary user comments about this <code class="docutils literal notranslate"><span class="pre">config</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">devices</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A list of <code class="docutils literal notranslate"><span class="pre">disk</span></code> or <code class="docutils literal notranslate"><span class="pre">volume</span></code> attachments for this <code class="docutils literal notranslate"><span class="pre">config</span></code>.  If the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code> omits a <code class="docutils literal notranslate"><span class="pre">devices</span></code> block, the Linode will not be booted.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sda</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - … <code class="docutils literal notranslate"><span class="pre">sdh</span></code> - (Optional) The SDA-SDH slots, represent the Linux block device nodes for the first 8 disks attached to the Linode.  Each device must be suplied sequentially.  The device can be either a Disk or a Volume identified by <code class="docutils literal notranslate"><span class="pre">disk_label</span></code> or <code class="docutils literal notranslate"><span class="pre">volume_id</span></code>. Only one disk identifier is permitted per slot. Devices mapped from <code class="docutils literal notranslate"><span class="pre">sde</span></code> through <code class="docutils literal notranslate"><span class="pre">sdh</span></code> are unavailable in <code class="docutils literal notranslate"><span class="pre">&quot;fullvirt&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">virt_mode</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdb</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdc</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdd</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sde</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdf</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdg</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdh</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">helpers</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Helpers enabled when booting to this Linode Config.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">devtmpfsAutomount</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">distro</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Controls the behavior of the Linode Config’s Distribution Helper setting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modulesDep</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Creates a modules dependency file for the Kernel you run.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Controls the behavior of the Linode Config’s Network Helper setting, used to automatically configure additional IP addresses assigned to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updatedbDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Disables updatedb cron job to avoid disk thrashing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kernel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - - A Kernel ID to boot a Linode with. Default is based on image choice. Examples are <code class="docutils literal notranslate"><span class="pre">linode/latest-64bit</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/grub2</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/direct-disk</span></code>, etc. See all kernels <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - - Defaults to the total RAM of the Linode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootDevice</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - - The root device to boot. The corresponding disk must be attached to a <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.  Example: <code class="docutils literal notranslate"><span class="pre">&quot;/dev/sda&quot;</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - - Defines the state of your Linode after booting. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - - Controls the virtualization mode. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;paravirt&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.group">
<code class="sig-name descname">group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The display group of the Linode instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.image">
<code class="sig-name descname">image</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.image" title="Permalink to this definition">¶</a></dt>
<dd><p>An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. See all images <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.ip_address">
<code class="sig-name descname">ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>This Linode’s Public IPv4 Address. If there are multiple public IPv4 addresses on this Instance, an arbitrary address
will be used for this field.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.ipv4s">
<code class="sig-name descname">ipv4s</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>This Linode’s IPv4 Addresses. Each Linode is assigned a single public IPv4 address upon creation, and may get a single
private IPv4 address if needed. You may need to open a support ticket to get additional IPv4 addresses.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.ipv6">
<code class="sig-name descname">ipv6</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>This Linode’s IPv6 SLAAC addresses. This address is specific to a Linode, and may not be shared.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.private_ip">
<code class="sig-name descname">private_ip</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>This Linode’s Private IPv4 Address. The regional private IP address range is 192.168.128/17 address shared by all Linode
Instances in a region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc. See all regions <a class="reference external" href="https://api.linode.com/v4/regions">here</a>. <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.root_pass">
<code class="sig-name descname">root_pass</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.root_pass" title="Permalink to this definition">¶</a></dt>
<dd><p>The password that will be initialially assigned to the ‘root’ user account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.stackscript_data">
<code class="sig-name descname">stackscript_data</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.stackscript_data" title="Permalink to this definition">¶</a></dt>
<dd><p>An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.stackscript_id">
<code class="sig-name descname">stackscript_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.stackscript_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the instance, indicating the current readiness state.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.swap_size">
<code class="sig-name descname">swap_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.swap_size" title="Permalink to this definition">¶</a></dt>
<dd><p>When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Linode type defines the pricing, CPU, disk, and RAM specs of the instance. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc. See all types <a class="reference external" href="https://api.linode.com/v4/linode/types">here</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Instance.watchdog_enabled">
<code class="sig-name descname">watchdog_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.watchdog_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alerts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">boot_config_label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_pass</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stackscript_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stackscript_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">swap_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">watchdog_enabled</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>authorized_users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>backup_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A Backup ID from another Linode’s available backups. Your User must have read_write access to that Linode, the Backup must have a status of successful, and the Linode must be deployed to the same region as the Backup. See /linode/instances/{linodeId}/backups for a Linode’s available backups. This field and the image field are mutually exclusive. <em>This value can not be imported.</em> <em>Changing ``backup_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>backups</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about this Linode’s backups status.</p></li>
<li><p><strong>backups_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.</p></li>
<li><p><strong>boot_config_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em></p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration profiles define the VM settings and boot behavior of the Linode Instance.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display group of the Linode instance.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. See all images <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p>
</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Linode’s Public IPv4 Address. If there are multiple public IPv4 addresses on this Instance, an arbitrary address
will be used for this field.</p></li>
<li><p><strong>ipv4s</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – This Linode’s IPv4 Addresses. Each Linode is assigned a single public IPv4 address upon creation, and may get a single
private IPv4 address if needed. You may need to open a support ticket to get additional IPv4 addresses.</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Linode’s IPv6 SLAAC addresses. This address is specific to a Linode, and may not be shared.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Linode’s Private IPv4 Address. The regional private IP address range is 192.168.128/17 address shared by all Linode
Instances in a region.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc. See all regions <a class="reference external" href="https://api.linode.com/v4/regions">here</a>. <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.</p>
</p></li>
<li><p><strong>root_pass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password that will be initialially assigned to the ‘root’ user account.</p></li>
<li><p><strong>stackscript_data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>stackscript_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the instance, indicating the current readiness state.</p></li>
<li><p><strong>swap_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Linode type defines the pricing, CPU, disk, and RAM specs of the instance. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc. See all types <a class="reference external" href="https://api.linode.com/v4/linode/types">here</a>.</p>
</p></li>
<li><p><strong>watchdog_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>alerts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">io</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkOut</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transferQuota</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>backups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Arbitrary user comments about this <code class="docutils literal notranslate"><span class="pre">config</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">devices</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of <code class="docutils literal notranslate"><span class="pre">disk</span></code> or <code class="docutils literal notranslate"><span class="pre">volume</span></code> attachments for this <code class="docutils literal notranslate"><span class="pre">config</span></code>.  If the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code> omits a <code class="docutils literal notranslate"><span class="pre">devices</span></code> block, the Linode will not be booted.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sda</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - … <code class="docutils literal notranslate"><span class="pre">sdh</span></code> - (Optional) The SDA-SDH slots, represent the Linux block device nodes for the first 8 disks attached to the Linode.  Each device must be suplied sequentially.  The device can be either a Disk or a Volume identified by <code class="docutils literal notranslate"><span class="pre">disk_label</span></code> or <code class="docutils literal notranslate"><span class="pre">volume_id</span></code>. Only one disk identifier is permitted per slot. Devices mapped from <code class="docutils literal notranslate"><span class="pre">sde</span></code> through <code class="docutils literal notranslate"><span class="pre">sdh</span></code> are unavailable in <code class="docutils literal notranslate"><span class="pre">&quot;fullvirt&quot;</span></code> <code class="docutils literal notranslate"><span class="pre">virt_mode</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sde</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sdh</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Disk ID of the associated <code class="docutils literal notranslate"><span class="pre">disk_label</span></code>, if used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">label</span></code> of the <code class="docutils literal notranslate"><span class="pre">disk</span></code> to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Volume ID to map to this <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">helpers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Helpers enabled when booting to this Linode Config.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">devtmpfsAutomount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">distro</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Controls the behavior of the Linode Config’s Distribution Helper setting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modulesDep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Creates a modules dependency file for the Kernel you run.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Controls the behavior of the Linode Config’s Network Helper setting, used to automatically configure additional IP addresses assigned to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updatedbDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Disables updatedb cron job to avoid disk thrashing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kernel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - A Kernel ID to boot a Linode with. Default is based on image choice. Examples are <code class="docutils literal notranslate"><span class="pre">linode/latest-64bit</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/grub2</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/direct-disk</span></code>, etc. See all kernels <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - - Defaults to the total RAM of the Linode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootDevice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - The root device to boot. The corresponding disk must be attached to a <code class="docutils literal notranslate"><span class="pre">device</span></code> slot.  Example: <code class="docutils literal notranslate"><span class="pre">&quot;/dev/sda&quot;</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">runLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Defines the state of your Linode after booting. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Controls the virtualization mode. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;paravirt&quot;</span></code>.</p></li>
</ul>
<p>The <strong>disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorized_users</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filesystem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the disk in the Linode API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. See all images <a class="reference external" href="https://api.linode.com/v4/linode/kernels">here</a>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">root_pass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Disk in MB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackscript_data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackscript_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p></li>
</ul>
<p>The <strong>specs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transfer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">LkeCluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">k8s_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.LkeCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an LKE cluster.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">LkeCluster</span><span class="p">(</span><span class="s2">&quot;my-cluster&quot;</span><span class="p">,</span>
    <span class="n">k8s_version</span><span class="o">=</span><span class="s2">&quot;1.17&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;my-cluster&quot;</span><span class="p">,</span>
    <span class="n">pools</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;count&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;g6-standard-2&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
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
<li><p><strong>pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional nested attributes:</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Kubernetes cluster’s location.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes in the Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the underlying Linode instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the node.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A Linode Type for all of the nodes in the Node Pool.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_linode.LkeCluster.api_endpoints">
<code class="sig-name descname">api_endpoints</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.LkeCluster.api_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoints for the Kubernetes API server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.LkeCluster.k8s_version">
<code class="sig-name descname">k8s_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.LkeCluster.k8s_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired Kubernetes version for this Kubernetes cluster in the format of <code class="docutils literal notranslate"><span class="pre">major.minor</span></code> (e.g. <code class="docutils literal notranslate"><span class="pre">1.17</span></code>), and the latest supported patch version will be deployed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.LkeCluster.kubeconfig">
<code class="sig-name descname">kubeconfig</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.LkeCluster.kubeconfig" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 encoded kubeconfig for the Kubernetes cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.LkeCluster.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.LkeCluster.label" title="Permalink to this definition">¶</a></dt>
<dd><p>This Kubernetes cluster’s unique label.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.LkeCluster.pools">
<code class="sig-name descname">pools</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.LkeCluster.pools" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional nested attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of nodes in the Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The ID of the underlying Linode instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The status of the node.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A Linode Type for all of the nodes in the Node Pool.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.LkeCluster.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.LkeCluster.region" title="Permalink to this definition">¶</a></dt>
<dd><p>This Kubernetes cluster’s location.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.LkeCluster.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.LkeCluster.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.LkeCluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.LkeCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.LkeCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">k8s_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.LkeCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LkeCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The endpoints for the Kubernetes API server.</p></li>
<li><p><strong>k8s_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired Kubernetes version for this Kubernetes cluster in the format of <code class="docutils literal notranslate"><span class="pre">major.minor</span></code> (e.g. <code class="docutils literal notranslate"><span class="pre">1.17</span></code>), and the latest supported patch version will be deployed.</p></li>
<li><p><strong>kubeconfig</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 encoded kubeconfig for the Kubernetes cluster.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Kubernetes cluster’s unique label.</p></li>
<li><p><strong>pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional nested attributes:</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This Kubernetes cluster’s location.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the node.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes in the Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the underlying Linode instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the node.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A Linode Type for all of the nodes in the Node Pool.</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_conn_throttle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NodeBalancer resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] client_conn_throttle: Throttle connections per second (0-20). Set to 0 (default) to disable throttling.
:param pulumi.Input[str] label: The label of the Linode NodeBalancer
:param pulumi.Input[str] region: The region where this NodeBalancer will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode NodeBalancer.</em>.
:param pulumi.Input[list] tags: A list of tags applied to this object. Tags are for organizational purposes only.</p>
<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancer.client_conn_throttle">
<code class="sig-name descname">client_conn_throttle</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.client_conn_throttle" title="Permalink to this definition">¶</a></dt>
<dd><p>Throttle connections per second (0-20). Set to 0 (default) to disable throttling.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancer.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>This NodeBalancer’s hostname, ending with .nodebalancer.linode.com</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancer.ipv4">
<code class="sig-name descname">ipv4</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The Public IPv4 Address of this NodeBalancer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancer.ipv6">
<code class="sig-name descname">ipv6</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>The Public IPv6 Address of this NodeBalancer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancer.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode NodeBalancer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancer.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where this NodeBalancer will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode NodeBalancer.</em>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_conn_throttle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transfer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_conn_throttle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Throttle connections per second (0-20). Set to 0 (default) to disable throttling.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This NodeBalancer’s hostname, ending with .nodebalancer.linode.com</p></li>
<li><p><strong>ipv4</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Public IPv4 Address of this NodeBalancer</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Public IPv6 Address of this NodeBalancer</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode NodeBalancer</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this NodeBalancer will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode NodeBalancer.</em>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>transfer</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">in_</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">out</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">total</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancerConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_passive</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cipher_suite</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodebalancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NodeBalancerConfig resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] algorithm: What algorithm this NodeBalancer should use for routing traffic to backends: roundrobin, leastconn, source
:param pulumi.Input[str] check: The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected.
:param pulumi.Input[float] check_attempts: How many times to attempt a check before considering a backend to be down. (1-30)
:param pulumi.Input[str] check_body: This value must be present in the response body of the check in order for it to pass. If this value is not present in</p>
<blockquote>
<div><p>the response body of a check request, the backend is considered to be down</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>check_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in seconds, to check that backends are up and serving requests.</p></li>
<li><p><strong>check_passive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, any response from this backend with a 5xx status code will be enough for it to be considered unhealthy and taken out of rotation.</p></li>
<li><p><strong>check_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.</p></li>
<li><p><strong>check_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long, in seconds, to wait for a check attempt before considering it failed. (1-30)</p></li>
<li><p><strong>cipher_suite</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What ciphers to use for SSL connections served by this NodeBalancer. <code class="docutils literal notranslate"><span class="pre">legacy</span></code> is considered insecure and should only be used if necessary.</p></li>
<li><p><strong>nodebalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the NodeBalancer to access.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TCP port this Config is for. These values must be unique across configs on a single NodeBalancer (you can’t have two configs for port 80, for example). While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. (Defaults to 80)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol this port is configured to serve. If this is set to https you must include an ssl_cert and an ssl_key. (Defaults to “http”)</p></li>
<li><p><strong>ssl_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate this port is serving. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p></li>
<li><p><strong>ssl_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key corresponding to this port’s certificate. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p></li>
<li><p><strong>stickiness</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how session stickiness is handled on this port: ‘none’, ‘table’, ‘http_cookie’</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.algorithm">
<code class="sig-name descname">algorithm</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>What algorithm this NodeBalancer should use for routing traffic to backends: roundrobin, leastconn, source</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check">
<code class="sig-name descname">check</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_attempts">
<code class="sig-name descname">check_attempts</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>How many times to attempt a check before considering a backend to be down. (1-30)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_body">
<code class="sig-name descname">check_body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_body" title="Permalink to this definition">¶</a></dt>
<dd><p>This value must be present in the response body of the check in order for it to pass. If this value is not present in
the response body of a check request, the backend is considered to be down</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_interval">
<code class="sig-name descname">check_interval</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in seconds, to check that backends are up and serving requests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_passive">
<code class="sig-name descname">check_passive</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_passive" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, any response from this backend with a 5xx status code will be enough for it to be considered unhealthy and taken out of rotation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_path">
<code class="sig-name descname">check_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_timeout">
<code class="sig-name descname">check_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>How long, in seconds, to wait for a check attempt before considering it failed. (1-30)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.cipher_suite">
<code class="sig-name descname">cipher_suite</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.cipher_suite" title="Permalink to this definition">¶</a></dt>
<dd><p>What ciphers to use for SSL connections served by this NodeBalancer. <code class="docutils literal notranslate"><span class="pre">legacy</span></code> is considered insecure and should only be used if necessary.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.nodebalancer_id">
<code class="sig-name descname">nodebalancer_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.nodebalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancer to access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The TCP port this Config is for. These values must be unique across configs on a single NodeBalancer (you can’t have two configs for port 80, for example). While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. (Defaults to 80)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol this port is configured to serve. If this is set to https you must include an ssl_cert and an ssl_key. (Defaults to “http”)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_cert">
<code class="sig-name descname">ssl_cert</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate this port is serving. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_commonname">
<code class="sig-name descname">ssl_commonname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_commonname" title="Permalink to this definition">¶</a></dt>
<dd><p>The common name for the SSL certification this port is serving if this port is not configured to use SSL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_fingerprint">
<code class="sig-name descname">ssl_fingerprint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint for the SSL certification this port is serving if this port is not configured to use SSL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_key">
<code class="sig-name descname">ssl_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key corresponding to this port’s certificate. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerConfig.stickiness">
<code class="sig-name descname">stickiness</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.stickiness" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls how session stickiness is handled on this port: ‘none’, ‘table’, ‘http_cookie’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_passive</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cipher_suite</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodebalancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_commonname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeBalancerConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<li><p><strong>ssl_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate this port is serving. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p></li>
<li><p><strong>ssl_commonname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The common name for the SSL certification this port is serving if this port is not configured to use SSL.</p></li>
<li><p><strong>ssl_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint for the SSL certification this port is serving if this port is not configured to use SSL.</p></li>
<li><p><strong>ssl_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key corresponding to this port’s certificate. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p></li>
<li><p><strong>stickiness</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how session stickiness is handled on this port: ‘none’, ‘table’, ‘http_cookie’</p></li>
</ul>
</dd>
</dl>
<p>The <strong>node_status</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status_down</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_up</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancerNode</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodebalancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NodeBalancerNode resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] address: The private IP Address where this backend can be reached. This must be a private IP address.
:param pulumi.Input[float] config_id: The ID of the NodeBalancerConfig to access.
:param pulumi.Input[str] label: The label of the Linode NodeBalancer Node. This is for display purposes only.
:param pulumi.Input[str] mode: The mode this NodeBalancer should use when sending traffic to this backend. If set to <code class="docutils literal notranslate"><span class="pre">accept</span></code> this backend is accepting traffic. If set to <code class="docutils literal notranslate"><span class="pre">reject</span></code> this backend will not receive traffic. If set to <code class="docutils literal notranslate"><span class="pre">drain</span></code> this backend will not receive new traffic, but connections already pinned to it will continue to be routed to it
:param pulumi.Input[float] nodebalancer_id: The ID of the NodeBalancer to access.
:param pulumi.Input[float] weight: Used when picking a backend to serve a request and is not pinned to a single backend yet. Nodes with a higher weight will receive more traffic. (1-255).</p>
<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerNode.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP Address where this backend can be reached. This must be a private IP address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerNode.config_id">
<code class="sig-name descname">config_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancerConfig to access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerNode.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode NodeBalancer Node. This is for display purposes only.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerNode.mode">
<code class="sig-name descname">mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode this NodeBalancer should use when sending traffic to this backend. If set to <code class="docutils literal notranslate"><span class="pre">accept</span></code> this backend is accepting traffic. If set to <code class="docutils literal notranslate"><span class="pre">reject</span></code> this backend will not receive traffic. If set to <code class="docutils literal notranslate"><span class="pre">drain</span></code> this backend will not receive new traffic, but connections already pinned to it will continue to be routed to it</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerNode.nodebalancer_id">
<code class="sig-name descname">nodebalancer_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.nodebalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancer to access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerNode.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of this node, based on the configured checks of its NodeBalancer Config. (unknown, UP, DOWN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.NodeBalancerNode.weight">
<code class="sig-name descname">weight</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Used when picking a backend to serve a request and is not pinned to a single backend yet. Nodes with a higher weight will receive more traffic. (1-255).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.NodeBalancerNode.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodebalancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeBalancerNode resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">ObjectStorageBucket</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Object Storage Bucket resource. This can be used to create, modify, and delete Linodes Object Storage Buckets.</p>
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
<dl class="py attribute">
<dt id="pulumi_linode.ObjectStorageBucket.cluster">
<code class="sig-name descname">cluster</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster of the Linode Object Storage Bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.ObjectStorageBucket.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode Object Storage Bucket.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageBucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ObjectStorageBucket resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster of the Linode Object Storage Bucket.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode Object Storage Bucket.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">ObjectStorageKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Object Storage Key resource. This can be used to create, modify, and delete Linodes Object Storage Keys.</p>
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
<dl class="py attribute">
<dt id="pulumi_linode.ObjectStorageKey.access_key">
<code class="sig-name descname">access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>This keypair’s access key. This is not secret.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.ObjectStorageKey.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label given to this key. For display purposes only.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.ObjectStorageKey.secret_key">
<code class="sig-name descname">secret_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>This keypair’s secret key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.ObjectStorageKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ObjectStorageKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This keypair’s access key. This is not secret.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label given to this key. For display purposes only.</p></li>
<li><p><strong>secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This keypair’s secret key.</p></li>
</ul>
</dd>
</dl>
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
<dt id="pulumi_linode.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ua_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Provider" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Rdns</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rdns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode RDNS resource.  This can be used to create and modify RDNS records.</p>
<p>Linode RDNS names must have a matching address value in an A or AAAA record.  This A or AAAA name must be resolvable at the time the RDNS resource is being associated.</p>
<p>For more information, see the <a class="reference external" href="https://developers.linode.com/api/docs/v4#operation/updateIP">Linode APIv4 docs</a> and the <a class="reference external" href="https://www.linode.com/docs/networking/dns/configure-your-linode-for-reverse-dns-classic-manager/">Configure your Linode for Reverse DNS</a> guide.</p>
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
<dl class="py attribute">
<dt id="pulumi_linode.Rdns.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Rdns.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Public IPv4 or IPv6 address that will receive the <code class="docutils literal notranslate"><span class="pre">PTR</span></code> record.  A matching <code class="docutils literal notranslate"><span class="pre">A</span></code> or <code class="docutils literal notranslate"><span class="pre">AAAA</span></code> record must exist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Rdns.rdns">
<code class="sig-name descname">rdns</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Rdns.rdns" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the RDNS address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Rdns.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rdns</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rdns resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Public IPv4 or IPv6 address that will receive the <code class="docutils literal notranslate"><span class="pre">PTR</span></code> record.  A matching <code class="docutils literal notranslate"><span class="pre">A</span></code> or <code class="docutils literal notranslate"><span class="pre">AAAA</span></code> record must exist.</p></li>
<li><p><strong>rdns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the RDNS address.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_linode.SshKey.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.SshKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this key was added.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.SshKey.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.SshKey.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A label for the SSH Key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.SshKey.ssh_key">
<code class="sig-name descname">ssh_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.SshKey.ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this key was added.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the SSH Key.</p></li>
<li><p><strong>ssh_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">StackScript</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rev_note</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a StackScript resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: A description for the StackScript.
:param pulumi.Input[list] images: An array of Image IDs representing the Images that this StackScript is compatible for deploying with.
:param pulumi.Input[bool] is_public: This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em>
:param pulumi.Input[str] label: The StackScript’s label is for display purposes only.
:param pulumi.Input[str] rev_note: This field allows you to add notes for the set of revisions made to this StackScript.
:param pulumi.Input[str] script: The script to execute when provisioning a new Linode with this StackScript.
:param pulumi.Input[list] user_defined_fields: This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized</p>
<blockquote>
<div><p>parameters during deployment.</p>
</div></blockquote>
<p>The <strong>user_defined_fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">example</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The StackScript’s label is for display purposes only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manyOf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneOf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_linode.StackScript.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this StackScript was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.deployments_active">
<code class="sig-name descname">deployments_active</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.deployments_active" title="Permalink to this definition">¶</a></dt>
<dd><p>Count of currently active, deployed Linodes created from this StackScript.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.deployments_total">
<code class="sig-name descname">deployments_total</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.deployments_total" title="Permalink to this definition">¶</a></dt>
<dd><p>The total number of times this StackScript has been deployed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the StackScript.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.images">
<code class="sig-name descname">images</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.images" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.is_public">
<code class="sig-name descname">is_public</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The StackScript’s label is for display purposes only.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.rev_note">
<code class="sig-name descname">rev_note</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.rev_note" title="Permalink to this definition">¶</a></dt>
<dd><p>This field allows you to add notes for the set of revisions made to this StackScript.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.script">
<code class="sig-name descname">script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.script" title="Permalink to this definition">¶</a></dt>
<dd><p>The script to execute when provisioning a new Linode with this StackScript.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.updated">
<code class="sig-name descname">updated</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this StackScript was updated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.user_defined_fields">
<code class="sig-name descname">user_defined_fields</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.user_defined_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized
parameters during deployment.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">example</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The StackScript’s label is for display purposes only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manyOf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneOf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.user_gravatar_id">
<code class="sig-name descname">user_gravatar_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.user_gravatar_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Gravatar ID for the User who created the StackScript.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.StackScript.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The User who created the StackScript.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.StackScript.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployments_active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployments_total</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rev_note</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_gravatar_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StackScript resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this StackScript was created.</p></li>
<li><p><strong>deployments_active</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Count of currently active, deployed Linodes created from this StackScript.</p></li>
<li><p><strong>deployments_total</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The total number of times this StackScript has been deployed.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the StackScript.</p></li>
<li><p><strong>images</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em></p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The StackScript’s label is for display purposes only.</p></li>
<li><p><strong>rev_note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field allows you to add notes for the set of revisions made to this StackScript.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script to execute when provisioning a new Linode with this StackScript.</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this StackScript was updated.</p></li>
<li><p><strong>user_defined_fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized
parameters during deployment.</p></li>
<li><p><strong>user_gravatar_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Gravatar ID for the User who created the StackScript.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The User who created the StackScript.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>user_defined_fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">example</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The StackScript’s label is for display purposes only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manyOf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneOf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Token</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Token resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] expiry: When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.
:param pulumi.Input[str] label: A label for the Token.
:param pulumi.Input[str] scopes: The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id17"><span class="problematic" id="id18">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p>
<dl class="py attribute">
<dt id="pulumi_linode.Token.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Token.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time this token was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Token.expiry">
<code class="sig-name descname">expiry</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Token.expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Token.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Token.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A label for the Token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Token.scopes">
<code class="sig-name descname">scopes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Token.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id19"><span class="problematic" id="id20">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Token.token">
<code class="sig-name descname">token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Token.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token used to access the API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Token.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Token resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time this token was created.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the Token.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id21"><span class="problematic" id="id22">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token used to access the API.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Volume resource.  This can be used to create, modify, and delete Linodes Block Storage Volumes.  Block Storage Volumes are removable storage disks that persist outside the life-cycle of Linode Instances. These volumes can be attached to and detached from Linode instances throughout a region.</p>
<p>For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/block-storage/how-to-use-block-storage-with-your-linode/">How to Use Block Storage with Your Linode</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createVolume">Linode APIv4 docs</a>.</p>
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
<li><p><strong>linode_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of a Linode Instance where the the Volume should be attached.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this volume will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Volume.</em>.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the Volume in GB.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_linode.Volume.filesystem_path">
<code class="sig-name descname">filesystem_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.filesystem_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The full filesystem path for the Volume based on the Volume’s label. Path is /dev/disk/by-id/scsi-0Linode<em>Volume</em> +
Volume label.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Volume.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode Volume</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Volume.linode_id">
<code class="sig-name descname">linode_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.linode_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Linode Instance where the the Volume should be attached.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Volume.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where this volume will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Volume.</em>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Volume.size">
<code class="sig-name descname">size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the Volume in GB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Volume.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the volume, indicating the current readiness state.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_linode.Volume.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_linode.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filesystem_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linode_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>filesystem_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full filesystem path for the Volume based on the Volume’s label. Path is /dev/disk/by-id/scsi-0Linode<em>Volume</em> +
Volume label.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode Volume</p></li>
<li><p><strong>linode_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of a Linode Instance where the the Volume should be attached.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this volume will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Volume.</em>.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the Volume in GB.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the volume, indicating the current readiness state.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode account.</p>
<p>This data source should not be used in conjuction with the <code class="docutils literal notranslate"><span class="pre">LINODE_DEBUG</span></code> option.  See the <a class="reference external" href="https://www.terraform.io/docs/providers/linode/index.html#debugging">debugging notes</a> for more details.</p>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_domain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode domain.</p>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_domain_record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_domain_record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Domain Record.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">my_record</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_domain_record</span><span class="p">(</span><span class="n">domain_id</span><span class="o">=</span><span class="s2">&quot;3150401&quot;</span><span class="p">,</span>
    <span class="nb">id</span><span class="o">=</span><span class="s2">&quot;14950401&quot;</span><span class="p">)</span>
<span class="n">my_www_record</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_domain_record</span><span class="p">(</span><span class="n">domain_id</span><span class="o">=</span><span class="s2">&quot;3150401&quot;</span><span class="p">,</span>
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
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_image">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode image</p>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_instance_type</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode instance type</p>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_networking_ip</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_networking_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Networking IP Address</p>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_object_storage_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_site_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_object_storage_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Object Storage Cluster</p>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_profile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode profile.</p>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_region</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_region" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getRegion</span></code> provides details about a specific Linode region.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">region</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_region</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;us-east&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_ssh_key">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_ssh_key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.SshKey</span></code> provides access to a specifically labeled SSH Key in the Profile of the User identified by the access token.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_ssh_key</span><span class="p">(</span><span class="n">label</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_stack_script">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_stack_script</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_stack_script" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Linode StackScript.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
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
<p>The <strong>user_defined_fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">example</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manyOf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneOf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_linode.get_user">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode user</p>
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
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Volume.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_linode</span> <span class="k">as</span> <span class="nn">linode</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">linode</span><span class="o">.</span><span class="n">get_volume</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;1234567&quot;</span><span class="p">)</span>
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
</dd></dl>

</div>
