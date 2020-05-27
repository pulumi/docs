---
title: Module wafv2
title_tag: Module wafv2 | Package pulumi_aws | Python SDK
linktitle: wafv2
notitle: true
---

<div class="section" id="wafv2">
<h1>wafv2<a class="headerlink" href="#wafv2" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.wafv2"></span><dl class="py class">
<dt id="pulumi_aws.wafv2.AwaitableGetIpSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafv2.</code><code class="sig-name descname">AwaitableGetIpSetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.AwaitableGetIpSetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.wafv2.AwaitableGetRegexPatternSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafv2.</code><code class="sig-name descname">AwaitableGetRegexPatternSetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regular_expressions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.AwaitableGetRegexPatternSetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.wafv2.GetIpSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafv2.</code><code class="sig-name descname">GetIpSetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.GetIpSetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpSet.</p>
<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetIpSetResult.addresses">
<code class="sig-name descname">addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetIpSetResult.addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings that specify one or more IP addresses or blocks of IP addresses in Classless Inter-Domain Routing (CIDR) notation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetIpSetResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetIpSetResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the entity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetIpSetResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetIpSetResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the set that helps with identification.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetIpSetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetIpSetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetIpSetResult.ip_address_version">
<code class="sig-name descname">ip_address_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetIpSetResult.ip_address_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address version of the set.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.wafv2.GetRegexPatternSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafv2.</code><code class="sig-name descname">GetRegexPatternSetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regular_expressions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.GetRegexPatternSetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegexPatternSet.</p>
<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetRegexPatternSetResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetRegexPatternSetResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the entity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetRegexPatternSetResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetRegexPatternSetResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the set that helps with identification.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetRegexPatternSetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetRegexPatternSetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.GetRegexPatternSetResult.regular_expressions">
<code class="sig-name descname">regular_expressions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.GetRegexPatternSetResult.regular_expressions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more blocks of regular expression patterns that AWS WAF is searching for. See Regular Expression below for details.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.wafv2.IpSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafv2.</code><code class="sig-name descname">IpSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.IpSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAFv2 IP Set Resource</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">wafv2</span><span class="o">.</span><span class="n">IpSet</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">addresses</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;1.2.3.4/32&quot;</span><span class="p">,</span>
        <span class="s2">&quot;5.6.7.8/32&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Example IP set&quot;</span><span class="p">,</span>
    <span class="n">ip_address_version</span><span class="o">=</span><span class="s2">&quot;IPV4&quot;</span><span class="p">,</span>
    <span class="n">scope</span><span class="o">=</span><span class="s2">&quot;REGIONAL&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Tag1&quot;</span><span class="p">:</span> <span class="s2">&quot;Value1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Tag2&quot;</span><span class="p">:</span> <span class="s2">&quot;Value2&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Contains an array of strings that specify one or more IP addresses or blocks of IP addresses in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all address ranges for IP versions IPv4 and IPv6.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly description of the IP set.</p></li>
<li><p><strong>ip_address_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify IPV4 or IPV6. Valid values are <code class="docutils literal notranslate"><span class="pre">IPV4</span></code> or <code class="docutils literal notranslate"><span class="pre">IPV6</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name of the IP set.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are <code class="docutils literal notranslate"><span class="pre">CLOUDFRONT</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. To work with CloudFront, you must also specify the Region US East (N. Virginia).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An array of key:value pairs to associate with the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.wafv2.IpSet.addresses">
<code class="sig-name descname">addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains an array of strings that specify one or more IP addresses or blocks of IP addresses in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all address ranges for IP versions IPv4 and IPv6.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.IpSet.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) that identifies the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.IpSet.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly description of the IP set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.IpSet.ip_address_version">
<code class="sig-name descname">ip_address_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.ip_address_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify IPV4 or IPV6. Valid values are <code class="docutils literal notranslate"><span class="pre">IPV4</span></code> or <code class="docutils literal notranslate"><span class="pre">IPV6</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.IpSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name of the IP set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.IpSet.scope">
<code class="sig-name descname">scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are <code class="docutils literal notranslate"><span class="pre">CLOUDFRONT</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. To work with CloudFront, you must also specify the Region US East (N. Virginia).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.IpSet.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of key:value pairs to associate with the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.wafv2.IpSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lock_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Contains an array of strings that specify one or more IP addresses or blocks of IP addresses in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports all address ranges for IP versions IPv4 and IPv6.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) that identifies the cluster.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly description of the IP set.</p></li>
<li><p><strong>ip_address_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify IPV4 or IPV6. Valid values are <code class="docutils literal notranslate"><span class="pre">IPV4</span></code> or <code class="docutils literal notranslate"><span class="pre">IPV6</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name of the IP set.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are <code class="docutils literal notranslate"><span class="pre">CLOUDFRONT</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. To work with CloudFront, you must also specify the Region US East (N. Virginia).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An array of key:value pairs to associate with the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.wafv2.IpSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafv2.IpSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.IpSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafv2.RegexPatternSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.wafv2.</code><code class="sig-name descname">RegexPatternSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regular_expressions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS WAFv2 Regex Pattern Set Resource</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">wafv2</span><span class="o">.</span><span class="n">RegexPatternSet</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Example regex pattern set&quot;</span><span class="p">,</span>
    <span class="n">regular_expressions</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;regexString&quot;</span><span class="p">:</span> <span class="s2">&quot;one&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;regexString&quot;</span><span class="p">:</span> <span class="s2">&quot;two&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">scope</span><span class="o">=</span><span class="s2">&quot;REGIONAL&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Tag1&quot;</span><span class="p">:</span> <span class="s2">&quot;Value1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Tag2&quot;</span><span class="p">:</span> <span class="s2">&quot;Value2&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly description of the regular expression pattern set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name of the regular expression pattern set.</p></li>
<li><p><strong>regular_expressions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more blocks of regular expression patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>. See Regular Expression below for details.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are <code class="docutils literal notranslate"><span class="pre">CLOUDFRONT</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. To work with CloudFront, you must also specify the region <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> (N. Virginia) on the AWS provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An array of key:value pairs to associate with the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>regular_expressions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regexString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The string representing the regular expression, see the AWS WAF <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-set-creating.html">documentation</a> for more information.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.wafv2.RegexPatternSet.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) that identifies the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.RegexPatternSet.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly description of the regular expression pattern set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.RegexPatternSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name of the regular expression pattern set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.RegexPatternSet.regular_expressions">
<code class="sig-name descname">regular_expressions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.regular_expressions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more blocks of regular expression patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>. See Regular Expression below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regexString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The string representing the regular expression, see the AWS WAF <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-set-creating.html">documentation</a> for more information.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.RegexPatternSet.scope">
<code class="sig-name descname">scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are <code class="docutils literal notranslate"><span class="pre">CLOUDFRONT</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. To work with CloudFront, you must also specify the region <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> (N. Virginia) on the AWS provider.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.wafv2.RegexPatternSet.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of key:value pairs to associate with the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.wafv2.RegexPatternSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lock_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regular_expressions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegexPatternSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) that identifies the cluster.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly description of the regular expression pattern set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name of the regular expression pattern set.</p></li>
<li><p><strong>regular_expressions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more blocks of regular expression patterns that you want AWS WAF to search for, such as <code class="docutils literal notranslate"><span class="pre">B[a&#64;]dB[o0]t</span></code>. See Regular Expression below for details.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are <code class="docutils literal notranslate"><span class="pre">CLOUDFRONT</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. To work with CloudFront, you must also specify the region <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> (N. Virginia) on the AWS provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An array of key:value pairs to associate with the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>regular_expressions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regexString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The string representing the regular expression, see the AWS WAF <a class="reference external" href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-set-creating.html">documentation</a> for more information.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.wafv2.RegexPatternSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafv2.RegexPatternSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.RegexPatternSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.wafv2.get_ip_set">
<code class="sig-prename descclassname">pulumi_aws.wafv2.</code><code class="sig-name descname">get_ip_set</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.get_ip_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieves the summary of a WAFv2 IP Set.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">wafv2</span><span class="o">.</span><span class="n">get_ip_set</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;some-ip-set&quot;</span><span class="p">,</span>
    <span class="n">scope</span><span class="o">=</span><span class="s2">&quot;REGIONAL&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the WAFv2 IP Set.</p></li>
<li><p><strong>scope</strong> (<em>str</em>) – Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are <code class="docutils literal notranslate"><span class="pre">CLOUDFRONT</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. To work with CloudFront, you must also specify the region <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> (N. Virginia) on the AWS provider.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.wafv2.get_regex_pattern_set">
<code class="sig-prename descclassname">pulumi_aws.wafv2.</code><code class="sig-name descname">get_regex_pattern_set</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.wafv2.get_regex_pattern_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieves the summary of a WAFv2 Regex Pattern Set.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">wafv2</span><span class="o">.</span><span class="n">get_regex_pattern_set</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;some-regex-pattern-set&quot;</span><span class="p">,</span>
    <span class="n">scope</span><span class="o">=</span><span class="s2">&quot;REGIONAL&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the WAFv2 Regex Pattern Set.</p></li>
<li><p><strong>scope</strong> (<em>str</em>) – Specifies whether this is for an AWS CloudFront distribution or for a regional application. Valid values are <code class="docutils literal notranslate"><span class="pre">CLOUDFRONT</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. To work with CloudFront, you must also specify the region <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> (N. Virginia) on the AWS provider.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
