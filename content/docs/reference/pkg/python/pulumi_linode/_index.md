---
title: Package pulumi_linode
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
<span class="target" id="module-pulumi_linode"></span><dl class="class">
<dt id="pulumi_linode.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">address1=None</em>, <em class="sig-param">address2=None</em>, <em class="sig-param">balance=None</em>, <em class="sig-param">city=None</em>, <em class="sig-param">company=None</em>, <em class="sig-param">country=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">phone=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">zip=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetDomainResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetDomainResult</code><span class="sig-paren">(</span><em class="sig-param">axfr_ips=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">expire_sec=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">master_ips=None</em>, <em class="sig-param">refresh_sec=None</em>, <em class="sig-param">retry_sec=None</em>, <em class="sig-param">soa_email=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl_sec=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetDomainResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em class="sig-param">created=None</em>, <em class="sig-param">created_by=None</em>, <em class="sig-param">deprecated=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vendor=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetInstanceTypeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetInstanceTypeResult</code><span class="sig-paren">(</span><em class="sig-param">addons=None</em>, <em class="sig-param">class_=None</em>, <em class="sig-param">disk=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">memory=None</em>, <em class="sig-param">network_out=None</em>, <em class="sig-param">price=None</em>, <em class="sig-param">transfer=None</em>, <em class="sig-param">vcpus=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetInstanceTypeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetNetworkingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetNetworkingIpResult</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">linode_id=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">public=None</em>, <em class="sig-param">rdns=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_mask=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetNetworkingIpResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetObjectStorageClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetObjectStorageClusterResult</code><span class="sig-paren">(</span><em class="sig-param">domain=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">static_site_domain=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetObjectStorageClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetProfileResult</code><span class="sig-paren">(</span><em class="sig-param">authorized_keys=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">email_notifications=None</em>, <em class="sig-param">ip_whitelist_enabled=None</em>, <em class="sig-param">lish_auth_method=None</em>, <em class="sig-param">referrals=None</em>, <em class="sig-param">restricted=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">two_factor_auth=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetProfileResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetRegionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetRegionResult</code><span class="sig-paren">(</span><em class="sig-param">country=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetRegionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param">created=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">ssh_key=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param">email=None</em>, <em class="sig-param">restricted=None</em>, <em class="sig-param">ssh_keys=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_linode.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">axfr_ips=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">expire_sec=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">master_ips=None</em>, <em class="sig-param">refresh_sec=None</em>, <em class="sig-param">retry_sec=None</em>, <em class="sig-param">soa_email=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl_sec=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Domain resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/domain.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/domain.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.Domain.axfr_ips">
<code class="sig-name descname">axfr_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.axfr_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of IPs that may perform a zone transfer for this Domain. This is potentially dangerous, and should be set to an empty list unless you intend to use it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this Domain. This is for display purposes only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain this Domain represents. These must be unique in our system; you cannot have two Domains representing the same domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.expire_sec">
<code class="sig-name descname">expire_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.expire_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time in seconds that may pass before this Domain is no longer authoritative. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.group">
<code class="sig-name descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The group this Domain belongs to. This is for display purposes only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.master_ips">
<code class="sig-name descname">master_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.master_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP addresses representing the master DNS for this Domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.refresh_sec">
<code class="sig-name descname">refresh_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.refresh_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time in seconds before this Domain should be refreshed. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.retry_sec">
<code class="sig-name descname">retry_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.retry_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval, in seconds, at which a failed refresh should be retried. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.soa_email">
<code class="sig-name descname">soa_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.soa_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Start of Authority email address. This is required for master Domains.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to control whether this Domain is currently being rendered (defaults to “active”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.ttl_sec">
<code class="sig-name descname">ttl_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.ttl_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Domain.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Domain.type" title="Permalink to this definition">¶</a></dt>
<dd><p>If this Domain represents the authoritative source of information for the domain it describes, or if it is a read-only copy of a master (also called a slave).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">axfr_ips=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">expire_sec=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">master_ips=None</em>, <em class="sig-param">refresh_sec=None</em>, <em class="sig-param">retry_sec=None</em>, <em class="sig-param">soa_email=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl_sec=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain.get" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/domain.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/domain.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.DomainRecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">DomainRecord</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">record_type=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">ttl_sec=None</em>, <em class="sig-param">weight=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Domain Record resource.  This can be used to create, modify, and delete Linodes Domain Records.
For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/manager/dns-manager/">DNS Manager</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createDomainRecord">Linode APIv4 docs</a>.</p>
<p>This resource exports no additional attributes.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Domain to access.  <em>Changing ``domain_id`` forces the creation of a new Linode Domain Record.</em>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the subdomain being associated with an IP address.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port this Record points to.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the target host. Lower values are preferred.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol this Record’s service communicates with. Only valid for SRV records.</p></li>
<li><p><strong>record_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. <em>Changing ``record_type`` forces the creation of a new Linode Domain Record.</em>.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service this Record identified. Only valid for SRV records.</p></li>
<li><p><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag portion of a CAA record. It is invalid to set this on other record types.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target for this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="o">-</span> <span class="o">-</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ttl_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The relative weight of this Record. Higher values are preferred.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/domain_record.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/domain_record.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Domain to access.  <em>Changing ``domain_id`` forces the creation of a new Linode Domain Record.</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the subdomain being associated with an IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port this Record points to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the target host. Lower values are preferred.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol this Record’s service communicates with. Only valid for SRV records.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.record_type">
<code class="sig-name descname">record_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.record_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. <em>Changing ``record_type`` forces the creation of a new Linode Domain Record.</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The service this Record identified. Only valid for SRV records.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.tag">
<code class="sig-name descname">tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag portion of a CAA record. It is invalid to set this on other record types.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.target">
<code class="sig-name descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The target for this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.ttl_sec">
<code class="sig-name descname">ttl_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.ttl_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.DomainRecord.weight">
<code class="sig-name descname">weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.DomainRecord.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>The relative weight of this Record. Higher values are preferred.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.DomainRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">record_type=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">ttl_sec=None</em>, <em class="sig-param">weight=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Domain to access.  <em>Changing ``domain_id`` forces the creation of a new Linode Domain Record.</em>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the subdomain being associated with an IP address.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port this Record points to.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the target host. Lower values are preferred.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol this Record’s service communicates with. Only valid for SRV records.</p></li>
<li><p><strong>record_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. <em>Changing ``record_type`` forces the creation of a new Linode Domain Record.</em>.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service this Record identified. Only valid for SRV records.</p></li>
<li><p><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag portion of a CAA record. It is invalid to set this on other record types.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target for this Record. This field’s actual usage depends on the type of record this represents. For A and AAAA records, this is the address the named Domain should resolve to.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="o">-</span> <span class="o">-</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ttl_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ‘Time to Live’ - the amount of time in seconds that this Domain’s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The relative weight of this Record. Higher values are preferred.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/domain_record.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/domain_record.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.DomainRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.DomainRecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.DomainRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">address1=None</em>, <em class="sig-param">address2=None</em>, <em class="sig-param">balance=None</em>, <em class="sig-param">city=None</em>, <em class="sig-param">company=None</em>, <em class="sig-param">country=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">phone=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">zip=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_linode.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetDomainResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetDomainResult</code><span class="sig-paren">(</span><em class="sig-param">axfr_ips=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">expire_sec=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">master_ips=None</em>, <em class="sig-param">refresh_sec=None</em>, <em class="sig-param">retry_sec=None</em>, <em class="sig-param">soa_email=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">ttl_sec=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetDomainResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomain.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param">created=None</em>, <em class="sig-param">created_by=None</em>, <em class="sig-param">deprecated=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vendor=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetInstanceTypeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetInstanceTypeResult</code><span class="sig-paren">(</span><em class="sig-param">addons=None</em>, <em class="sig-param">class_=None</em>, <em class="sig-param">disk=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">memory=None</em>, <em class="sig-param">network_out=None</em>, <em class="sig-param">price=None</em>, <em class="sig-param">transfer=None</em>, <em class="sig-param">vcpus=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetInstanceTypeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceType.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetNetworkingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetNetworkingIpResult</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">linode_id=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">public=None</em>, <em class="sig-param">rdns=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_mask=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetNetworkingIpResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkingIp.</p>
<dl class="attribute">
<dt id="pulumi_linode.GetNetworkingIpResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetNetworkingIpResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetObjectStorageClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetObjectStorageClusterResult</code><span class="sig-paren">(</span><em class="sig-param">domain=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">static_site_domain=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetObjectStorageClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getObjectStorageCluster.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetProfileResult</code><span class="sig-paren">(</span><em class="sig-param">authorized_keys=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">email_notifications=None</em>, <em class="sig-param">ip_whitelist_enabled=None</em>, <em class="sig-param">lish_auth_method=None</em>, <em class="sig-param">referrals=None</em>, <em class="sig-param">restricted=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">two_factor_auth=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProfile.</p>
<dl class="attribute">
<dt id="pulumi_linode.GetProfileResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetRegionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetRegionResult</code><span class="sig-paren">(</span><em class="sig-param">country=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetRegionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegion.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param">created=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">ssh_key=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKey.</p>
<dl class="attribute">
<dt id="pulumi_linode.GetSshKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetSshKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_linode.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param">email=None</em>, <em class="sig-param">restricted=None</em>, <em class="sig-param">ssh_keys=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_linode.GetUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_linode.Image">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">linode_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Image resource.  This can be used to create, modify, and delete Linodes Images.  Linode Images are snapshots of a Linode Instance Disk which can then be used to provision more Linode Instances.  Images can be used across regions.</p>
<p>For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/disk-images/linode-images/">Linode’s documentation on Images</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createImage">Linode APIv4 docs</a>.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/image.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/image.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.Image.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A detailed description of this Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Image.disk_id">
<code class="sig-name descname">disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Linode Disk that this Image will be created from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Image.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the Image. Labels cannot contain special characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Image.linode_id">
<code class="sig-name descname">linode_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Image.linode_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Linode that this Image will be created from.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Image.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">created_by=None</em>, <em class="sig-param">deprecated=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_id=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">linode_id=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vendor=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Image resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A detailed description of this Image.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Linode Disk that this Image will be created from.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the Image. Labels cannot contain special characters.</p></li>
<li><p><strong>linode_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the Linode that this Image will be created from.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/image.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Image.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Image.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alerts=None</em>, <em class="sig-param">authorized_keys=None</em>, <em class="sig-param">authorized_users=None</em>, <em class="sig-param">backup_id=None</em>, <em class="sig-param">backups_enabled=None</em>, <em class="sig-param">boot_config_label=None</em>, <em class="sig-param">configs=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">image=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">private_ip=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">root_pass=None</em>, <em class="sig-param">stackscript_data=None</em>, <em class="sig-param">stackscript_id=None</em>, <em class="sig-param">swap_size=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">watchdog_enabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Instance resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>authorized_users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>backup_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A Backup ID from another Linode’s available backups. Your User must have read_write access to that Linode, the Backup must have a status of successful, and the Linode must be deployed to the same region as the Backup. See /linode/instances/{linodeId}/backups for a Linode’s available backups. This field and the image field are mutually exclusive. <em>This value can not be imported.</em> <em>Changing ``backup_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>backups_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.</p></li>
<li><p><strong>boot_config_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em></p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display group of the Linode instance.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.</p></li>
<li><p><strong>stackscript_data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>stackscript_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>swap_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Linode type defines the pricing, CPU, disk, and RAM specs of the instance.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc.</p></li>
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
<p>The <strong>configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Arbitrary user comments about this <code class="docutils literal notranslate"><span class="pre">config</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">devices</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of <code class="docutils literal notranslate"><span class="pre">disk</span></code> or <code class="docutils literal notranslate"><span class="pre">volume</span></code> attachments for this <code class="docutils literal notranslate"><span class="pre">config</span></code>.  If the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code> omits a <code class="docutils literal notranslate"><span class="pre">devices</span></code> block, the Linode will not be booted.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sda</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">kernel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - A Kernel ID to boot a Linode with. Default is based on image choice. (examples: linode/latest-64bit, linode/grub2, linode/direct-disk)</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">filesystem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the disk in the Linode API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">root_pass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Disk in MB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackscript_data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackscript_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/instance.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.Instance.authorized_keys">
<code class="sig-name descname">authorized_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.authorized_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SSH public keys to deploy for the root user on the newly created Linode. Only accepted if <code class="docutils literal notranslate"><span class="pre">image</span></code> is provided. <em>This value can not be imported.</em> <em>Changing ``authorized_keys`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.authorized_users">
<code class="sig-name descname">authorized_users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.authorized_users" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Linode usernames. If the usernames have associated SSH keys, the keys will be appended to the <code class="docutils literal notranslate"><span class="pre">root</span></code> user’s <code class="docutils literal notranslate"><span class="pre">~/.ssh/authorized_keys</span></code> file automatically. <em>This value can not be imported.</em> <em>Changing ``authorized_users`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.backup_id">
<code class="sig-name descname">backup_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.backup_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A Backup ID from another Linode’s available backups. Your User must have read_write access to that Linode, the Backup must have a status of successful, and the Linode must be deployed to the same region as the Backup. See /linode/instances/{linodeId}/backups for a Linode’s available backups. This field and the image field are mutually exclusive. <em>This value can not be imported.</em> <em>Changing ``backup_id`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.backups_enabled">
<code class="sig-name descname">backups_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.backups_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.boot_config_label">
<code class="sig-name descname">boot_config_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.boot_config_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.group">
<code class="sig-name descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The display group of the Linode instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.image">
<code class="sig-name descname">image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.image" title="Permalink to this definition">¶</a></dt>
<dd><p>An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.private_ip">
<code class="sig-name descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.stackscript_data">
<code class="sig-name descname">stackscript_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.stackscript_data" title="Permalink to this definition">¶</a></dt>
<dd><p>An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.stackscript_id">
<code class="sig-name descname">stackscript_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.stackscript_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.swap_size">
<code class="sig-name descname">swap_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.swap_size" title="Permalink to this definition">¶</a></dt>
<dd><p>When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Linode type defines the pricing, CPU, disk, and RAM specs of the instance.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Instance.watchdog_enabled">
<code class="sig-name descname">watchdog_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Instance.watchdog_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alerts=None</em>, <em class="sig-param">authorized_keys=None</em>, <em class="sig-param">authorized_users=None</em>, <em class="sig-param">backup_id=None</em>, <em class="sig-param">backups=None</em>, <em class="sig-param">backups_enabled=None</em>, <em class="sig-param">boot_config_label=None</em>, <em class="sig-param">configs=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">group=None</em>, <em class="sig-param">image=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ipv4s=None</em>, <em class="sig-param">ipv6=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">private_ip=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">root_pass=None</em>, <em class="sig-param">specs=None</em>, <em class="sig-param">stackscript_data=None</em>, <em class="sig-param">stackscript_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">swap_size=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">watchdog_enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>backups_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this field is set to true, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.</p></li>
<li><p><strong>boot_config_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Label of the Instance Config that should be used to boot the Linode instance.  If there is only one <code class="docutils literal notranslate"><span class="pre">config</span></code>, the <code class="docutils literal notranslate"><span class="pre">label</span></code> of that <code class="docutils literal notranslate"><span class="pre">config</span></code> will be used as the <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>. <em>This value can not be imported.</em></p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display group of the Linode instance.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the created Linode will have private networking enabled, allowing use of the 192.168.128.0/17 network within the Linode’s region. It can be enabled on an existing Linode but it can’t be disabled.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the location where the Linode is deployed. Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Instance.</em>.</p></li>
<li><p><strong>stackscript_data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An object containing responses to any User Defined Fields present in the StackScript being deployed to this Linode. Only accepted if ‘stackscript_id’ is given. The required values depend on the StackScript being deployed.  <em>This value can not be imported.</em> <em>Changing ``stackscript_data`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>stackscript_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The StackScript to deploy to the newly created Linode. If provided, ‘image’ must also be provided, and must be an Image that is compatible with this StackScript. <em>This value can not be imported.</em> <em>Changing ``stackscript_id`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><strong>swap_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – When deploying from an Image, this field is optional with a Linode API default of 512mb, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Linode type defines the pricing, CPU, disk, and RAM specs of the instance.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;g6-nanode-1&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-standard-2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-highmem-16&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;g6-dedicated-16&quot;</span></code>, etc.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">sda</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">kernel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - A Kernel ID to boot a Linode with. Default is based on image choice. (examples: linode/latest-64bit, linode/grub2, linode/direct-disk)</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">filesystem</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the disk in the Linode API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An Image ID to deploy the Disk from. Official Linode Images start with linode/, while your Images start with private/. See /images for more information on the Images available for you to use. Examples are <code class="docutils literal notranslate"><span class="pre">linode/debian9</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/fedora28</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/ubuntu16.04lts</span></code>, <code class="docutils literal notranslate"><span class="pre">linode/arch</span></code>, and <code class="docutils literal notranslate"><span class="pre">private/12345</span></code>. <em>Changing ``image`` forces the creation of a new Linode Instance.</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Config’s label for display purposes.  Also used by <code class="docutils literal notranslate"><span class="pre">boot_config_label</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">root_pass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <span class="raw-html-m2r"><elided></span></p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/instance.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_conn_throttle=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NodeBalancer resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_conn_throttle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Throttle connections per second (0-20). Set to 0 (default) to disable throttling.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode NodeBalancer</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this NodeBalancer will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode NodeBalancer.</em>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.NodeBalancer.client_conn_throttle">
<code class="sig-name descname">client_conn_throttle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.client_conn_throttle" title="Permalink to this definition">¶</a></dt>
<dd><p>Throttle connections per second (0-20). Set to 0 (default) to disable throttling.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancer.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode NodeBalancer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancer.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where this NodeBalancer will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode NodeBalancer.</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancer.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.NodeBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_conn_throttle=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">ipv4=None</em>, <em class="sig-param">ipv6=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">transfer=None</em>, <em class="sig-param">updated=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_conn_throttle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Throttle connections per second (0-20). Set to 0 (default) to disable throttling.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.NodeBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancerConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancerConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">check=None</em>, <em class="sig-param">check_attempts=None</em>, <em class="sig-param">check_body=None</em>, <em class="sig-param">check_interval=None</em>, <em class="sig-param">check_passive=None</em>, <em class="sig-param">check_path=None</em>, <em class="sig-param">check_timeout=None</em>, <em class="sig-param">cipher_suite=None</em>, <em class="sig-param">nodebalancer_id=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">ssl_cert=None</em>, <em class="sig-param">ssl_key=None</em>, <em class="sig-param">stickiness=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NodeBalancerConfig resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What algorithm this NodeBalancer should use for routing traffic to backends: roundrobin, leastconn, source</p></li>
<li><p><strong>check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected.</p></li>
<li><p><strong>check_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How many times to attempt a check before considering a backend to be down. (1-30)</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer_config.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer_config.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.algorithm">
<code class="sig-name descname">algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>What algorithm this NodeBalancer should use for routing traffic to backends: roundrobin, leastconn, source</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check">
<code class="sig-name descname">check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. If none no check is performed. connection requires only a connection to the backend to succeed. http and http_body rely on the backend serving HTTP, and that the response returned matches what is expected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_attempts">
<code class="sig-name descname">check_attempts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>How many times to attempt a check before considering a backend to be down. (1-30)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_interval">
<code class="sig-name descname">check_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in seconds, to check that backends are up and serving requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_passive">
<code class="sig-name descname">check_passive</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_passive" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, any response from this backend with a 5xx status code will be enough for it to be considered unhealthy and taken out of rotation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_path">
<code class="sig-name descname">check_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.check_timeout">
<code class="sig-name descname">check_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.check_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>How long, in seconds, to wait for a check attempt before considering it failed. (1-30)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.cipher_suite">
<code class="sig-name descname">cipher_suite</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.cipher_suite" title="Permalink to this definition">¶</a></dt>
<dd><p>What ciphers to use for SSL connections served by this NodeBalancer. <code class="docutils literal notranslate"><span class="pre">legacy</span></code> is considered insecure and should only be used if necessary.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.nodebalancer_id">
<code class="sig-name descname">nodebalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.nodebalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancer to access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The TCP port this Config is for. These values must be unique across configs on a single NodeBalancer (you can’t have two configs for port 80, for example). While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. (Defaults to 80)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol this port is configured to serve. If this is set to https you must include an ssl_cert and an ssl_key. (Defaults to “http”)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_cert">
<code class="sig-name descname">ssl_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate this port is serving. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.ssl_key">
<code class="sig-name descname">ssl_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.ssl_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key corresponding to this port’s certificate. This is not returned. If set, this field will come back as <code class="docutils literal notranslate"><span class="pre">&lt;REDACTED&gt;</span></code>. Please use the ssl_commonname and ssl_fingerprint to identify the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerConfig.stickiness">
<code class="sig-name descname">stickiness</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.stickiness" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls how session stickiness is handled on this port: ‘none’, ‘table’, ‘http_cookie’</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.NodeBalancerConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">check=None</em>, <em class="sig-param">check_attempts=None</em>, <em class="sig-param">check_body=None</em>, <em class="sig-param">check_interval=None</em>, <em class="sig-param">check_passive=None</em>, <em class="sig-param">check_path=None</em>, <em class="sig-param">check_timeout=None</em>, <em class="sig-param">cipher_suite=None</em>, <em class="sig-param">node_status=None</em>, <em class="sig-param">nodebalancer_id=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">ssl_cert=None</em>, <em class="sig-param">ssl_commonname=None</em>, <em class="sig-param">ssl_fingerprint=None</em>, <em class="sig-param">ssl_key=None</em>, <em class="sig-param">stickiness=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.get" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>node_status</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status_down</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_up</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer_config.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer_config.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.NodeBalancerConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancerConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancerNode">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">NodeBalancerNode</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">config_id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">nodebalancer_id=None</em>, <em class="sig-param">weight=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NodeBalancerNode resource with the given unique name, props, and options.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer_node.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer_node.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerNode.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP Address where this backend can be reached. This must be a private IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerNode.config_id">
<code class="sig-name descname">config_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancerConfig to access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerNode.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode NodeBalancer Node. This is for display purposes only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerNode.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode this NodeBalancer should use when sending traffic to this backend. If set to <code class="docutils literal notranslate"><span class="pre">accept</span></code> this backend is accepting traffic. If set to <code class="docutils literal notranslate"><span class="pre">reject</span></code> this backend will not receive traffic. If set to <code class="docutils literal notranslate"><span class="pre">drain</span></code> this backend will not receive new traffic, but connections already pinned to it will continue to be routed to it</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerNode.nodebalancer_id">
<code class="sig-name descname">nodebalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.nodebalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NodeBalancer to access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.NodeBalancerNode.weight">
<code class="sig-name descname">weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Used when picking a backend to serve a request and is not pinned to a single backend yet. Nodes with a higher weight will receive more traffic. (1-255).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.NodeBalancerNode.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">config_id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">nodebalancer_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">weight=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Used when picking a backend to serve a request and is not pinned to a single backend yet. Nodes with a higher weight will receive more traffic. (1-255).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer_node.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/nodebalancer_node.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.NodeBalancerNode.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.NodeBalancerNode.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.NodeBalancerNode.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.ObjectStorageBucket">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">ObjectStorageBucket</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Object Storage Bucket resource. This can be used to create, modify, and delete Linodes Object Storage Buckets.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/object_storage_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/object_storage_bucket.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.ObjectStorageBucket.cluster">
<code class="sig-name descname">cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster of the Linode Object Storage Bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.ObjectStorageBucket.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode Object Storage Bucket.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.ObjectStorageBucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">label=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.get" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/object_storage_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/object_storage_bucket.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.ObjectStorageBucket.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.ObjectStorageBucket.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.ObjectStorageKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">ObjectStorageKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Object Storage Key resource. This can be used to create, modify, and delete Linodes Object Storage Keys.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/object_storage_key.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/object_storage_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.ObjectStorageKey.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label given to this key. For display purposes only.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.ObjectStorageKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">secret_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ObjectStorageKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label given to this key. For display purposes only.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/object_storage_key.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/object_storage_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.ObjectStorageKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.ObjectStorageKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.ObjectStorageKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_version=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">ua_prefix=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the linode package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_linode.Provider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Provider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Provider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Rdns">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Rdns</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">rdns=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/rdns.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/rdns.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.Rdns.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Rdns.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Public IPv4 or IPv6 address that will receive the <code class="docutils literal notranslate"><span class="pre">PTR</span></code> record.  A matching <code class="docutils literal notranslate"><span class="pre">A</span></code> or <code class="docutils literal notranslate"><span class="pre">AAAA</span></code> record must exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Rdns.rdns">
<code class="sig-name descname">rdns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Rdns.rdns" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the RDNS address.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Rdns.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">rdns=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns.get" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/rdns.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/rdns.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Rdns.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Rdns.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Rdns.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.SshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">ssh_key=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/sshkey.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/sshkey.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.SshKey.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.SshKey.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A label for the SSH Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.SshKey.ssh_key">
<code class="sig-name descname">ssh_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.SshKey.ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">ssh_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the SSH Key.</p></li>
<li><p><strong>ssh_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/sshkey.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/sshkey.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.SshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.SshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.StackScript">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">StackScript</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">images=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">rev_note=None</em>, <em class="sig-param">script=None</em>, <em class="sig-param">user_defined_fields=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a StackScript resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the StackScript.</p></li>
<li><p><strong>images</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em></p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The StackScript’s label is for display purposes only.</p></li>
<li><p><strong>rev_note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field allows you to add notes for the set of revisions made to this StackScript.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script to execute when provisioning a new Linode with this StackScript.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/stackscript.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/stackscript.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.StackScript.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the StackScript.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.StackScript.images">
<code class="sig-name descname">images</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.images" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.StackScript.is_public">
<code class="sig-name descname">is_public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.StackScript.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The StackScript’s label is for display purposes only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.StackScript.rev_note">
<code class="sig-name descname">rev_note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.rev_note" title="Permalink to this definition">¶</a></dt>
<dd><p>This field allows you to add notes for the set of revisions made to this StackScript.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.StackScript.script">
<code class="sig-name descname">script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.StackScript.script" title="Permalink to this definition">¶</a></dt>
<dd><p>The script to execute when provisioning a new Linode with this StackScript.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.StackScript.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">deployments_active=None</em>, <em class="sig-param">deployments_total=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">images=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">rev_note=None</em>, <em class="sig-param">script=None</em>, <em class="sig-param">updated=None</em>, <em class="sig-param">user_defined_fields=None</em>, <em class="sig-param">user_gravatar_id=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StackScript resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the StackScript.</p></li>
<li><p><strong>images</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of Image IDs representing the Images that this StackScript is compatible for deploying with.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. <em>Changing ``is_public`` forces the creation of a new StackScript</em></p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The StackScript’s label is for display purposes only.</p></li>
<li><p><strong>rev_note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field allows you to add notes for the set of revisions made to this StackScript.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script to execute when provisioning a new Linode with this StackScript.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/stackscript.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/stackscript.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.StackScript.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.StackScript.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.StackScript.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Token">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Token</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Token resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the Token.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id4"><span class="problematic" id="id5">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/token.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/token.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.Token.expiry">
<code class="sig-name descname">expiry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Token.expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Token.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Token.label" title="Permalink to this definition">¶</a></dt>
<dd><p>A label for the Token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Token.scopes">
<code class="sig-name descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Token.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id6"><span class="problematic" id="id7">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Token.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">token=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Token resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When this token will expire. Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated. Tokens may be created with ‘null’ as their expiry and will never expire unless revoked.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A label for the Token.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the Linode CLI, require tokens with access to <a href="#id8"><span class="problematic" id="id9">*</span></a>. Tokens with more restrictive scopes are generally more secure.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/token.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/token.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Token.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Token.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Token.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Volume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">linode_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Linode Volume resource.  This can be used to create, modify, and delete Linodes Block Storage Volumes.  Block Storage Volumes are removable storage disks that persist outside the life-cycle of Linode Instances. These volumes can be attached to and detached from Linode instances throughout a region.</p>
<p>For more information, see <a class="reference external" href="https://www.linode.com/docs/platform/block-storage/how-to-use-block-storage-with-your-linode/">How to Use Block Storage with Your Linode</a> and the <a class="reference external" href="https://developers.linode.com/api/v4#operation/createVolume">Linode APIv4 docs</a>.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/volume.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/volume.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_linode.Volume.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label of the Linode Volume</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Volume.linode_id">
<code class="sig-name descname">linode_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.linode_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Linode Instance where the the Volume should be attached.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Volume.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where this volume will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Volume.</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Volume.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the Volume in GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_linode.Volume.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_linode.Volume.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags applied to this object. Tags are for organizational purposes only.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">filesystem_path=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">linode_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label of the Linode Volume</p></li>
<li><p><strong>linode_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of a Linode Instance where the the Volume should be attached.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where this volume will be deployed.  Examples are <code class="docutils literal notranslate"><span class="pre">&quot;us-east&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;us-west&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ap-south&quot;</span></code>, etc.  <em>Changing ``region`` forces the creation of a new Linode Volume.</em>.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the Volume in GB.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags applied to this object. Tags are for organizational purposes only.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/volume.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/r/volume.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_linode.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.Volume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_linode.get_account">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode account.</p>
<p>This data source should not be used in conjuction with the <code class="docutils literal notranslate"><span class="pre">LINODE_DEBUG</span></code> option.  See the <a class="reference external" href="https://www.terraform.io/docs/providers/linode/index.html#debugging">debugging notes</a> for more details.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/account.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/account.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_domain">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_domain</code><span class="sig-paren">(</span><em class="sig-param">domain=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode domain.</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">retry_sec</span></code> - The interval, in seconds, at which a failed refresh should be retried.
*</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/domain.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/domain.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_image">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode image</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/image.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_instance_type">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_instance_type</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode instance type</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/instance_type.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/instance_type.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_networking_ip">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_networking_ip</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_networking_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Networking IP Address</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/networking_ip.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/networking_ip.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_object_storage_cluster">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_object_storage_cluster</code><span class="sig-paren">(</span><em class="sig-param">domain=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">static_site_domain=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_object_storage_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode Object Storage Cluster</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/object_storage_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/object_storage_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_profile">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_profile</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode profile.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/profile.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/profile.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_region">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_region</code><span class="sig-paren">(</span><em class="sig-param">country=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_region" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getRegion</span></code> provides details about a specific Linode region.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/region.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/region.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_ssh_key">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_ssh_key</code><span class="sig-paren">(</span><em class="sig-param">label=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.SshKey</span></code> provides access to a specifically labeled SSH Key in the Profile of the User identified by the access token.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/sshkey.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/sshkey.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_linode.get_user">
<code class="sig-prename descclassname">pulumi_linode.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param">username=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_linode.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Linode user</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/user.html.markdown">https://github.com/terraform-providers/terraform-provider-linode/blob/master/website/docs/d/user.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
