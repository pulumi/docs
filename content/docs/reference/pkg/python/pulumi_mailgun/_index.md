---
title: Package pulumi_mailgun
title_tag: Package pulumi_mailgun | Python SDK
linktitle: pulumi_mailgun
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "mailgun" >}}

<div class="section" id="pulumi-mailgun">
<h1>Pulumi Mailgun<a class="headerlink" href="#pulumi-mailgun" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mailgun">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-mailgun/issues">pulumi/pulumi-mailgun repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mailgun/issues">terraform-providers/terraform-provider-mailgun repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_mailgun"></span><dl class="py class">
<dt id="pulumi_mailgun.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mailgun.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spam_action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wildcard</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Mailgun App resource. This can be used to
create and manage applications on Mailgun.</p>
<p>After DNS records are set, domain verification should be triggered manually using <a class="reference external" href="https://documentation.mailgun.com/en/latest/api-domains.html#domains">PUT /domains/&lt;domain&amp;gt;/verify</a></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mailgun</span> <span class="k">as</span> <span class="nn">mailgun</span>

<span class="c1"># Create a new Mailgun domain</span>
<span class="n">default</span> <span class="o">=</span> <span class="n">mailgun</span><span class="o">.</span><span class="n">Domain</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us&quot;</span><span class="p">,</span>
    <span class="n">smtp_password</span><span class="o">=</span><span class="s2">&quot;supersecretpassword1234&quot;</span><span class="p">,</span>
    <span class="n">spam_action</span><span class="o">=</span><span class="s2">&quot;disabled&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Domains can be imported using <code class="docutils literal notranslate"><span class="pre">region:domain_name</span></code> via <code class="docutils literal notranslate"><span class="pre">import</span></code> command. Region has to be chosen from <code class="docutils literal notranslate"><span class="pre">eu</span></code> or <code class="docutils literal notranslate"><span class="pre">us</span></code> (when no selection <code class="docutils literal notranslate"><span class="pre">us</span></code> is applied).</p>
<p>hcl</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import mailgun:index/domain:Domain <span class="nb">test</span> us:example.domain.com
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to add to Mailgun</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where domain will be created. Default value is <code class="docutils literal notranslate"><span class="pre">us</span></code>.</p></li>
<li><p><strong>smtp_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for SMTP authentication</p></li>
<li><p><strong>spam_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">disabled</span></code> or <code class="docutils literal notranslate"><span class="pre">tag</span></code> Disable, no spam
filtering will occur for inbound messages. Tag, messages
will be tagged with a spam header.</p></li>
<li><p><strong>wildcard</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean that determines whether
the domain will accept email for sub-domains.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mailgun.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">receiving_records</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DomainReceivingRecordArgs, Mapping[str, Any], Awaitable[Union[DomainReceivingRecordArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DomainReceivingRecordArgs, Mapping[str, Any], Awaitable[Union[DomainReceivingRecordArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sending_records</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DomainSendingRecordArgs, Mapping[str, Any], Awaitable[Union[DomainSendingRecordArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DomainSendingRecordArgs, Mapping[str, Any], Awaitable[Union[DomainSendingRecordArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_login</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spam_action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wildcard</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mailgun.domain.Domain<a class="headerlink" href="#pulumi_mailgun.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to add to Mailgun</p></li>
<li><p><strong>receiving_records</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DomainReceivingRecordArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of DNS records for receiving validation.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where domain will be created. Default value is <code class="docutils literal notranslate"><span class="pre">us</span></code>.</p></li>
<li><p><strong>sending_records</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DomainSendingRecordArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of DNS records for sending validation.</p></li>
<li><p><strong>smtp_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The login email for the SMTP server.</p></li>
<li><p><strong>smtp_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for SMTP authentication</p></li>
<li><p><strong>spam_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">disabled</span></code> or <code class="docutils literal notranslate"><span class="pre">tag</span></code> Disable, no spam
filtering will occur for inbound messages. Tag, messages
will be tagged with a spam header.</p></li>
<li><p><strong>wildcard</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean that determines whether
the domain will accept email for sub-domains.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mailgun.Domain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain to add to Mailgun</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.receiving_records">
<em class="property">property </em><code class="sig-name descname">receiving_records</code><a class="headerlink" href="#pulumi_mailgun.Domain.receiving_records" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DNS records for receiving validation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_mailgun.Domain.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where domain will be created. Default value is <code class="docutils literal notranslate"><span class="pre">us</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.sending_records">
<em class="property">property </em><code class="sig-name descname">sending_records</code><a class="headerlink" href="#pulumi_mailgun.Domain.sending_records" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DNS records for sending validation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.smtp_login">
<em class="property">property </em><code class="sig-name descname">smtp_login</code><a class="headerlink" href="#pulumi_mailgun.Domain.smtp_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The login email for the SMTP server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.smtp_password">
<em class="property">property </em><code class="sig-name descname">smtp_password</code><a class="headerlink" href="#pulumi_mailgun.Domain.smtp_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for SMTP authentication</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.spam_action">
<em class="property">property </em><code class="sig-name descname">spam_action</code><a class="headerlink" href="#pulumi_mailgun.Domain.spam_action" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> or <code class="docutils literal notranslate"><span class="pre">tag</span></code> Disable, no spam
filtering will occur for inbound messages. Tag, messages
will be tagged with a spam header.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.wildcard">
<em class="property">property </em><code class="sig-name descname">wildcard</code><a class="headerlink" href="#pulumi_mailgun.Domain.wildcard" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean that determines whether
the domain will accept email for sub-domains.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mailgun.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mailgun.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mailgun.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the mailgun package. By default, resources use package-wide configuration
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
<dl class="py method">
<dt id="pulumi_mailgun.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mailgun.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mailgun.Route">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mailgun.</code><code class="sig-name descname">Route</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expression</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Mailgun Route resource. This can be used to create and manage routes on Mailgun.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mailgun</span> <span class="k">as</span> <span class="nn">mailgun</span>

<span class="c1"># Create a new Mailgun route</span>
<span class="n">default</span> <span class="o">=</span> <span class="n">mailgun</span><span class="o">.</span><span class="n">Route</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">actions</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;forward(&#39;http://example.com/api/v1/foos/&#39;)&quot;</span><span class="p">,</span>
        <span class="s2">&quot;stop()&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;inbound&quot;</span><span class="p">,</span>
    <span class="n">expression</span><span class="o">=</span><span class="s2">&quot;match_recipient(&#39;.*@foo.example.com&#39;)&quot;</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
</pre></div>
</div>
<p>Routes can be imported using <code class="docutils literal notranslate"><span class="pre">ROUTE_ID</span></code> and <code class="docutils literal notranslate"><span class="pre">region</span></code> via <code class="docutils literal notranslate"><span class="pre">import</span></code> command. Route ID can be found on Mailgun portal in section <code class="docutils literal notranslate"><span class="pre">Receiving/Routes</span></code>. Region has to be chosen from <code class="docutils literal notranslate"><span class="pre">eu</span></code> or <code class="docutils literal notranslate"><span class="pre">us</span></code> (when no selection <code class="docutils literal notranslate"><span class="pre">us</span></code> is applied).</p>
<p>hcl</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import mailgun:index/route:Route <span class="nb">test</span> eu:123456789
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A filter expression like <code class="docutils literal notranslate"><span class="pre">match_recipient('.*&#64;gmail.com')</span></code></p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Smaller number indicates higher priority. Higher priority routes are handled first.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where domain will be created. Default value is <code class="docutils literal notranslate"><span class="pre">us</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mailgun.Route.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expression</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mailgun.route.Route<a class="headerlink" href="#pulumi_mailgun.Route.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Route resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A filter expression like <code class="docutils literal notranslate"><span class="pre">match_recipient('.*&#64;gmail.com')</span></code></p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Smaller number indicates higher priority. Higher priority routes are handled first.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where domain will be created. Default value is <code class="docutils literal notranslate"><span class="pre">us</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Route.expression">
<em class="property">property </em><code class="sig-name descname">expression</code><a class="headerlink" href="#pulumi_mailgun.Route.expression" title="Permalink to this definition">¶</a></dt>
<dd><p>A filter expression like <code class="docutils literal notranslate"><span class="pre">match_recipient('.*&#64;gmail.com')</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Route.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_mailgun.Route.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Smaller number indicates higher priority. Higher priority routes are handled first.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Route.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_mailgun.Route.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where domain will be created. Default value is <code class="docutils literal notranslate"><span class="pre">us</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mailgun.Route.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mailgun.Route.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mailgun.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
