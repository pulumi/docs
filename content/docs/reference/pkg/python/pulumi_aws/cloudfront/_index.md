---
---

<div class="section" id="module-pulumi_aws.cloudfront">
<span id="cloudfront"></span><h1>cloudfront<a class="headerlink" href="#module-pulumi_aws.cloudfront" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.cloudfront.Distribution">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudfront.</code><code class="descname">Distribution</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>aliases=None</em>, <em>comment=None</em>, <em>custom_error_responses=None</em>, <em>default_cache_behavior=None</em>, <em>default_root_object=None</em>, <em>enabled=None</em>, <em>http_version=None</em>, <em>is_ipv6_enabled=None</em>, <em>logging_config=None</em>, <em>ordered_cache_behaviors=None</em>, <em>origins=None</em>, <em>origin_groups=None</em>, <em>price_class=None</em>, <em>restrictions=None</em>, <em>retain_on_delete=None</em>, <em>tags=None</em>, <em>viewer_certificate=None</em>, <em>wait_for_deployment=None</em>, <em>web_acl_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Amazon CloudFront web distribution.</p>
<p>For information about CloudFront distributions, see the
[Amazon CloudFront Developer Guide][1]. For specific information about creating
CloudFront web distributions, see the [POST Distribution][2] page in the Amazon
CloudFront API Reference.</p>
<blockquote>
<div><strong>NOTE:</strong> CloudFront distributions take about 15 minutes to a deployed state
after creation or modification. During this time, deletes to resources will be
blocked. If you need to delete a distribution that is enabled and you do not
want to wait, you need to use the <code class="docutils literal notranslate"><span class="pre">retain_on_delete</span></code> flag.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Extra CNAMEs (alternate domain names), if any, for
this distribution.</li>
<li><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any comments you want to include about the
distribution.</li>
<li><strong>custom_error_responses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more custom error response elements (multiples allowed).</li>
<li><strong>default_cache_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default cache behavior for this distribution (maximum
one).</li>
<li><strong>default_root_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the distribution is enabled to accept end
user requests for content.</li>
<li><strong>http_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum HTTP version to support on the
distribution. Allowed values are <code class="docutils literal notranslate"><span class="pre">http1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">http2</span></code>. The default is
<code class="docutils literal notranslate"><span class="pre">http2</span></code>.</li>
<li><strong>is_ipv6_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the IPv6 is enabled for the distribution.</li>
<li><strong>logging_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The logging
configuration that controls how logs are written
to your distribution (maximum one).</li>
<li><strong>ordered_cache_behaviors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.</li>
<li><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origins for this
distribution (multiples allowed).</li>
<li><strong>origin_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more origin_group for this
distribution (multiples allowed).</li>
<li><strong>price_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The price class for this distribution. One of
<code class="docutils literal notranslate"><span class="pre">PriceClass_All</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_200</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_100</span></code></li>
<li><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The restriction
configuration for this distribution (maximum one).</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>viewer_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The SSL
configuration for this distribution (maximum
one).</li>
<li><strong>wait_for_deployment</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the resource will wait for
the distribution status to change from <code class="docutils literal notranslate"><span class="pre">InProgress</span></code> to <code class="docutils literal notranslate"><span class="pre">Deployed</span></code>. Setting
this to<code class="docutils literal notranslate"><span class="pre">false</span></code> will skip the process. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>web_acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you’re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
<code class="docutils literal notranslate"><span class="pre">waf:GetWebACL</span></code> permissions assigned.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_distribution.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_distribution.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.active_trusted_signers">
<code class="descname">active_trusted_signers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.active_trusted_signers" title="Permalink to this definition">¶</a></dt>
<dd><p>The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.aliases">
<code class="descname">aliases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>Extra CNAMEs (alternate domain names), if any, for
this distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.caller_reference">
<code class="descname">caller_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future
updates to the distribution configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.comment">
<code class="descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Any comments you want to include about the
distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.custom_error_responses">
<code class="descname">custom_error_responses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.custom_error_responses" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more custom error response elements (multiples allowed).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.default_cache_behavior">
<code class="descname">default_cache_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.default_cache_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The default cache behavior for this distribution (maximum
one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.default_root_object">
<code class="descname">default_root_object</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.default_root_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS domain name of either the S3 bucket, or
web site of your custom origin.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the distribution is enabled to accept end
user requests for content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the distribution’s information. For example:
<code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.hosted_zone_id">
<code class="descname">hosted_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.hosted_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID <code class="docutils literal notranslate"><span class="pre">Z2FDTNDATAQYW2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.http_version">
<code class="descname">http_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.http_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum HTTP version to support on the
distribution. Allowed values are <code class="docutils literal notranslate"><span class="pre">http1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">http2</span></code>. The default is
<code class="docutils literal notranslate"><span class="pre">http2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.in_progress_validation_batches">
<code class="descname">in_progress_validation_batches</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.in_progress_validation_batches" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of invalidation batches
currently in progress.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.is_ipv6_enabled">
<code class="descname">is_ipv6_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.is_ipv6_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the IPv6 is enabled for the distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.last_modified_time">
<code class="descname">last_modified_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the distribution was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.logging_config">
<code class="descname">logging_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.logging_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging
configuration that controls how logs are written
to your distribution (maximum one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.ordered_cache_behaviors">
<code class="descname">ordered_cache_behaviors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.ordered_cache_behaviors" title="Permalink to this definition">¶</a></dt>
<dd><p>An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.origins">
<code class="descname">origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more origins for this
distribution (multiples allowed).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.origin_groups">
<code class="descname">origin_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.origin_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more origin_group for this
distribution (multiples allowed).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.price_class">
<code class="descname">price_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.price_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The price class for this distribution. One of
<code class="docutils literal notranslate"><span class="pre">PriceClass_All</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_200</span></code>, <code class="docutils literal notranslate"><span class="pre">PriceClass_100</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.restrictions">
<code class="descname">restrictions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.restrictions" title="Permalink to this definition">¶</a></dt>
<dd><p>The restriction
configuration for this distribution (maximum one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the distribution. <code class="docutils literal notranslate"><span class="pre">Deployed</span></code> if the
distribution’s information is fully propagated throughout the Amazon
CloudFront system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.viewer_certificate">
<code class="descname">viewer_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.viewer_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL
configuration for this distribution (maximum
one).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.wait_for_deployment">
<code class="descname">wait_for_deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.wait_for_deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled, the resource will wait for
the distribution status to change from <code class="docutils literal notranslate"><span class="pre">InProgress</span></code> to <code class="docutils literal notranslate"><span class="pre">Deployed</span></code>. Setting
this to<code class="docutils literal notranslate"><span class="pre">false</span></code> will skip the process. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.Distribution.web_acl_id">
<code class="descname">web_acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.web_acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If you’re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
<code class="docutils literal notranslate"><span class="pre">waf:GetWebACL</span></code> permissions assigned.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.Distribution.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.Distribution.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.Distribution.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudfront.</code><code class="descname">OriginAccessIdentity</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>comment=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Amazon CloudFront origin access identity.</p>
<p>For information about CloudFront distributions, see the
[Amazon CloudFront Developer Guide][1]. For more information on generating
origin access identities, see
[Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content][2].</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment for the origin access identity.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_origin_access_identity.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_origin_access_identity.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.caller_reference">
<code class="descname">caller_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future
updates to the origin access identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.cloudfront_access_identity_path">
<code class="descname">cloudfront_access_identity_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.cloudfront_access_identity_path" title="Permalink to this definition">¶</a></dt>
<dd><p>A shortcut to the full path for the
origin access identity to use in CloudFront, see below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.comment">
<code class="descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment for the origin access identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the origin access identity’s information.
For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.iam_arn">
<code class="descname">iam_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.iam_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A pre-generated ARN for use in S3 bucket policies (see below).
Example: <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::cloudfront:user/CloudFront</span> <span class="pre">Origin</span> <span class="pre">Access</span> <span class="pre">Identity</span>
<span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.s3_canonical_user_id">
<code class="descname">s3_canonical_user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.s3_canonical_user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon S3 canonical user ID for the origin
access identity, which you use when giving the origin access identity read
permission to an object in Amazon S3.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.OriginAccessIdentity.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.OriginAccessIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.PublicKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudfront.</code><code class="descname">PublicKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>comment=None</em>, <em>encoded_key=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PublicKey resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the public key.</li>
<li><strong>encoded_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encoded public key that you want to add to CloudFront to use with features like field-level encryption.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the public key. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_public_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_public_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.caller_reference">
<code class="descname">caller_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Internal value used by CloudFront to allow future updates to the public key configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.comment">
<code class="descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment about the public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.encoded_key">
<code class="descname">encoded_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.encoded_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The encoded public key that you want to add to CloudFront to use with features like field-level encryption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the public key. For example: <code class="docutils literal notranslate"><span class="pre">E2QWRUHAPOMQZL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudfront.PublicKey.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the public key. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudfront.PublicKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudfront.PublicKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudfront.PublicKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
