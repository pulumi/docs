---
title: Module cloudfront
---

<div class="section" id="cloudfront">
<h1>cloudfront<a class="headerlink" href="#cloudfront" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.cloudfront"></span><dl class="class">
<dt id="pulumi_aws.cloudfront.Distribution">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">Distribution</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aliases=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">custom_error_responses=None</em>, <em class="sig-param">default_cache_behavior=None</em>, <em class="sig-param">default_root_object=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">http_version=None</em>, <em class="sig-param">is_ipv6_enabled=None</em>, <em class="sig-param">logging_config=None</em>, <em class="sig-param">ordered_cache_behaviors=None</em>, <em class="sig-param">origins=None</em>, <em class="sig-param">origin_groups=None</em>, <em class="sig-param">price_class=None</em>, <em class="sig-param">restrictions=None</em>, <em class="sig-param">retain_on_delete=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">viewer_certificate=None</em>, <em class="sig-param">wait_for_deployment=None</em>, <em class="sig-param">web_acl_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Amazon CloudFront web distribution.</p>
<p>For information about CloudFront distributions, see the
[Amazon CloudFront Developer Guide][1]. For specific information about creating
CloudFront web distributions, see the [POST Distribution][2] page in the Amazon
CloudFront API Reference.</p>
<blockquote>
<div><p><strong>NOTE:</strong> CloudFront distributions take about 15 minutes to a deployed state
after creation or modification. During this time, deletes to resources will be
blocked. If you need to delete a distribution that is enabled and you do not
want to wait, you need to use the <code class="docutils literal notranslate"><span class="pre">retain_on_delete</span></code> flag.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Extra CNAMEs (alternate domain names), if any, for
this distribution.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any comments you want to include about the
distribution.</p></li>
<li><p><strong>custom_error_responses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more custom error response elements (multiples allowed).</p></li>
<li><p><strong>default_cache_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default cache behavior for this distribution (maximum
one).</p></li>
<li><p><strong>default_root_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the distribution is enabled to accept end
user requests for content.</p></li>
<li><p><strong>http_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum HTTP version to support on the
distribution. Allowed values are <code class="docutils literal notranslate"><span class="pre">http1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">http2</span></code>. The default is
<code class="docutils literal notranslate"><span class="pre">http2</span></code>.</p></li>
<li><p><strong>is_ipv6_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the IPv6 is enabled for the distribution.</p></li>
<li><p><strong>logging_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The logging
configuration that controls how logs are written
to your distribution (maximum one).</p></li>
<li><p><strong>ordered_cache_behaviors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origins for this
distribution (multiples allowed).</p></li>
<li><p><strong>origin_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origin_group for this
distribution (multiples allowed).</p></li>
<li><p><strong>price_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The price class for this distribution. One of
<code class="docutils literal notranslate"><span class="pre">PriceClass_All</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_200</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_100</span></code></p></li>
<li><p><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The restriction
configuration for this distribution (maximum one).</p></li>
<li><p><strong>retain_on_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>viewer_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The SSL
configuration for this distribution (maximum
one).</p></li>
<li><p><strong>wait_for_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the resource will wait for
the distribution status to change from <code class="docutils literal notranslate"><span class="pre">InProgress</span></code> to <code class="docutils literal notranslate"><span class="pre">Deployed</span></code>. Setting
this to<code class="docutils literal notranslate"><span class="pre">false</span></code> will skip the process. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>web_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you’re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
<code class="docutils literal notranslate"><span class="pre">waf:GetWebACL</span></code> permissions assigned.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_distribution.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_distribution.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.active_trusted_signers">
<code class="sig-name descname">active_trusted_signers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.active_trusted_signers" title="Permalink to this definition">¶</a></dt>
<dd><p>The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.aliases">
<code class="sig-name descname">aliases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>Extra CNAMEs (alternate domain names), if any, for
this distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.caller_reference">
<code class="sig-name descname">caller_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future
updates to the distribution configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Any comments you want to include about the
distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.custom_error_responses">
<code class="sig-name descname">custom_error_responses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.custom_error_responses" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more custom error response elements (multiples allowed).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.default_cache_behavior">
<code class="sig-name descname">default_cache_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.default_cache_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The default cache behavior for this distribution (maximum
one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.default_root_object">
<code class="sig-name descname">default_root_object</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.default_root_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS domain name of either the S3 bucket, or
web site of your custom origin.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the distribution is enabled to accept end
user requests for content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the distribution’s information. For example:
<code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.hosted_zone_id">
<code class="sig-name descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID <code class="docutils literal notranslate"><span class="pre">Z2FDTNDATAQYW2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.http_version">
<code class="sig-name descname">http_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.http_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum HTTP version to support on the
distribution. Allowed values are <code class="docutils literal notranslate"><span class="pre">http1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">http2</span></code>. The default is
<code class="docutils literal notranslate"><span class="pre">http2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.in_progress_validation_batches">
<code class="sig-name descname">in_progress_validation_batches</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.in_progress_validation_batches" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of invalidation batches
currently in progress.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.is_ipv6_enabled">
<code class="sig-name descname">is_ipv6_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.is_ipv6_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the IPv6 is enabled for the distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.last_modified_time">
<code class="sig-name descname">last_modified_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the distribution was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.logging_config">
<code class="sig-name descname">logging_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.logging_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging
configuration that controls how logs are written
to your distribution (maximum one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.ordered_cache_behaviors">
<code class="sig-name descname">ordered_cache_behaviors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.ordered_cache_behaviors" title="Permalink to this definition">¶</a></dt>
<dd><p>An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.origins">
<code class="sig-name descname">origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more origins for this
distribution (multiples allowed).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.origin_groups">
<code class="sig-name descname">origin_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.origin_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more origin_group for this
distribution (multiples allowed).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.price_class">
<code class="sig-name descname">price_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.price_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The price class for this distribution. One of
<code class="docutils literal notranslate"><span class="pre">PriceClass_All</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_200</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_100</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.restrictions">
<code class="sig-name descname">restrictions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.restrictions" title="Permalink to this definition">¶</a></dt>
<dd><p>The restriction
configuration for this distribution (maximum one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.retain_on_delete">
<code class="sig-name descname">retain_on_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.retain_on_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the distribution. <code class="docutils literal notranslate"><span class="pre">Deployed</span></code> if the
distribution’s information is fully propagated throughout the Amazon
CloudFront system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.viewer_certificate">
<code class="sig-name descname">viewer_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.viewer_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL
configuration for this distribution (maximum
one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.wait_for_deployment">
<code class="sig-name descname">wait_for_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.wait_for_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled, the resource will wait for
the distribution status to change from <code class="docutils literal notranslate"><span class="pre">InProgress</span></code> to <code class="docutils literal notranslate"><span class="pre">Deployed</span></code>. Setting
this to<code class="docutils literal notranslate"><span class="pre">false</span></code> will skip the process. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.web_acl_id">
<code class="sig-name descname">web_acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.web_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If you’re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
<code class="docutils literal notranslate"><span class="pre">waf:GetWebACL</span></code> permissions assigned.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.Distribution.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active_trusted_signers=None</em>, <em class="sig-param">aliases=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">caller_reference=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">custom_error_responses=None</em>, <em class="sig-param">default_cache_behavior=None</em>, <em class="sig-param">default_root_object=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">hosted_zone_id=None</em>, <em class="sig-param">http_version=None</em>, <em class="sig-param">in_progress_validation_batches=None</em>, <em class="sig-param">is_ipv6_enabled=None</em>, <em class="sig-param">last_modified_time=None</em>, <em class="sig-param">logging_config=None</em>, <em class="sig-param">ordered_cache_behaviors=None</em>, <em class="sig-param">origins=None</em>, <em class="sig-param">origin_groups=None</em>, <em class="sig-param">price_class=None</em>, <em class="sig-param">restrictions=None</em>, <em class="sig-param">retain_on_delete=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">viewer_certificate=None</em>, <em class="sig-param">wait_for_deployment=None</em>, <em class="sig-param">web_acl_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Distribution resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] active_trusted_signers: The key pair IDs that CloudFront is aware of for</p>
<blockquote>
<div><p>each trusted signer, if the distribution is set up to serve private content
with signed URLs.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Extra CNAMEs (alternate domain names), if any, for
this distribution.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.</p></li>
<li><p><strong>caller_reference</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internal value used by CloudFront to allow future
updates to the distribution configuration.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any comments you want to include about the
distribution.</p></li>
<li><p><strong>custom_error_responses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more custom error response elements (multiples allowed).</p></li>
<li><p><strong>default_cache_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default cache behavior for this distribution (maximum
one).</p></li>
<li><p><strong>default_root_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS domain name of either the S3 bucket, or
web site of your custom origin.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the distribution is enabled to accept end
user requests for content.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the distribution’s information. For example:
<code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p></li>
<li><p><strong>hosted_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID <code class="docutils literal notranslate"><span class="pre">Z2FDTNDATAQYW2</span></code>.</p></li>
<li><p><strong>http_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum HTTP version to support on the
distribution. Allowed values are <code class="docutils literal notranslate"><span class="pre">http1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">http2</span></code>. The default is
<code class="docutils literal notranslate"><span class="pre">http2</span></code>.</p></li>
<li><p><strong>in_progress_validation_batches</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of invalidation batches
currently in progress.</p></li>
<li><p><strong>is_ipv6_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the IPv6 is enabled for the distribution.</p></li>
<li><p><strong>last_modified_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time the distribution was last modified.</p></li>
<li><p><strong>logging_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The logging
configuration that controls how logs are written
to your distribution (maximum one).</p></li>
<li><p><strong>ordered_cache_behaviors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origins for this
distribution (multiples allowed).</p></li>
<li><p><strong>origin_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origin_group for this
distribution (multiples allowed).</p></li>
<li><p><strong>price_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The price class for this distribution. One of
<code class="docutils literal notranslate"><span class="pre">PriceClass_All</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_200</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_100</span></code></p></li>
<li><p><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The restriction
configuration for this distribution (maximum one).</p></li>
<li><p><strong>retain_on_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current status of the distribution. <code class="docutils literal notranslate"><span class="pre">Deployed</span></code> if the
distribution’s information is fully propagated throughout the Amazon
CloudFront system.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>viewer_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The SSL
configuration for this distribution (maximum
one).</p></li>
<li><p><strong>wait_for_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the resource will wait for
the distribution status to change from <code class="docutils literal notranslate"><span class="pre">InProgress</span></code> to <code class="docutils literal notranslate"><span class="pre">Deployed</span></code>. Setting
this to<code class="docutils literal notranslate"><span class="pre">false</span></code> will skip the process. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>web_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you’re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
<code class="docutils literal notranslate"><span class="pre">waf:GetWebACL</span></code> permissions assigned.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_distribution.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_distribution.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.Distribution.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.Distribution.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">OriginAccessIdentity</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Amazon CloudFront origin access identity.</p>
<p>For information about CloudFront distributions, see the
[Amazon CloudFront Developer Guide][1]. For more information on generating
origin access identities, see
[Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content][2].</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment for the origin access identity.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_origin_access_identity.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_origin_access_identity.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.caller_reference">
<code class="sig-name descname">caller_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future
updates to the origin access identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.cloudfront_access_identity_path">
<code class="sig-name descname">cloudfront_access_identity_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.cloudfront_access_identity_path" title="Permalink to this definition">¶</a></dt>
<dd><p>A shortcut to the full path for the
origin access identity to use in CloudFront, see below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment for the origin access identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the origin access identity’s information.
For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.iam_arn">
<code class="sig-name descname">iam_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.iam_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A pre-generated ARN for use in S3 bucket policies (see below).
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::cloudfront:user/CloudFront</span> <span class="pre">Origin</span> <span class="pre">Access</span> <span class="pre">Identity</span>
<span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.s3_canonical_user_id">
<code class="sig-name descname">s3_canonical_user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.s3_canonical_user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon S3 canonical user ID for the origin
access identity, which you use when giving the origin access identity read
permission to an object in Amazon S3.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">caller_reference=None</em>, <em class="sig-param">cloudfront_access_identity_path=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">iam_arn=None</em>, <em class="sig-param">s3_canonical_user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OriginAccessIdentity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] caller_reference: Internal value used by CloudFront to allow future</p>
<blockquote>
<div><p>updates to the origin access identity.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cloudfront_access_identity_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shortcut to the full path for the
origin access identity to use in CloudFront, see below.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment for the origin access identity.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the origin access identity’s information.
For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p></li>
<li><p><strong>iam_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A pre-generated ARN for use in S3 bucket policies (see below).
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::cloudfront:user/CloudFront</span> <span class="pre">Origin</span> <span class="pre">Access</span> <span class="pre">Identity</span>
<span class="pre">E2QWRUHAPOMQZL</span></code>.</p></li>
<li><p><strong>s3_canonical_user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon S3 canonical user ID for the origin
access identity, which you use when giving the origin access identity read
permission to an object in Amazon S3.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_origin_access_identity.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_origin_access_identity.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.PublicKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudfront.</code><code class="sig-name descname">PublicKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">encoded_key=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PublicKey resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the public key.</p></li>
<li><p><strong>encoded_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encoded public key that you want to add to CloudFront to use with features like field-level encryption.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the public key. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the public key. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_public_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_public_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.caller_reference">
<code class="sig-name descname">caller_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future updates to the public key configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment about the public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.encoded_key">
<code class="sig-name descname">encoded_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.encoded_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The encoded public key that you want to add to CloudFront to use with features like field-level encryption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the public key. For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the public key. By default generated by this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the public key. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.PublicKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">caller_reference=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">encoded_key=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PublicKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] caller_reference: Internal value used by CloudFront to allow future updates to the public key configuration.
:param pulumi.Input[str] comment: An optional comment about the public key.
:param pulumi.Input[str] encoded_key: The encoded public key that you want to add to CloudFront to use with features like field-level encryption.
:param pulumi.Input[str] etag: The current version of the public key. For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.
:param pulumi.Input[str] name: The name for the public key. By default generated by this provider.
:param pulumi.Input[str] name_prefix: The name for the public key. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_public_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_public_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.PublicKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.PublicKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
