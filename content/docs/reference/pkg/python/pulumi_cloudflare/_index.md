---
title: Package pulumi_cloudflare
title_tag: Package pulumi_cloudflare | Python SDK
linktitle: pulumi_cloudflare
notitle: true
---

<div class="section" id="pulumi-cloudflare">
<h1>Pulumi Cloudflare<a class="headerlink" href="#pulumi-cloudflare" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-cloudflare/issues">pulumi/pulumi-cloudflare repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/issues">terraform-providers/terraform-provider-cloudflare repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_cloudflare"></span><dl class="py class">
<dt id="pulumi_cloudflare.AccessApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessApplication</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Application resource. Access Applications
are used to restrict access to a whole application using an
authorisation gateway managed by Cloudflare.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">staging_app</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessApplication</span><span class="p">(</span><span class="s2">&quot;stagingApp&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;staging.example.com&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging application&quot;</span><span class="p">,</span>
    <span class="n">session_duration</span><span class="o">=</span><span class="s2">&quot;24h&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessApplication.aud">
<code class="sig-name descname">aud</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.aud" title="Permalink to this definition">¶</a></dt>
<dd><p>Application Audience (AUD) Tag of the application</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessApplication.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessApplication.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessApplication.session_duration">
<code class="sig-name descname">session_duration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessApplication.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aud</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessApplication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aud</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Audience (AUD) Tag of the application</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requires</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Group resource. Access Groups are used
in conjunction with Access Policies to restrict access to a
particular resource based on group membership.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Allowing access to `test@example.com` email address only</span>
<span class="n">test_group_access_group</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessGroup</span><span class="p">(</span><span class="s2">&quot;testGroupAccessGroup&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;975ecf5a45e3bcb680dba0722a420ad9&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging group&quot;</span><span class="p">,</span>
    <span class="n">include</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;emails&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">],</span>
    <span class="p">}])</span>
<span class="c1"># Allowing `test@example.com` to access but only when coming from a</span>
<span class="c1"># specific IP.</span>
<span class="n">test_group_index_access_group_access_group</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessGroup</span><span class="p">(</span><span class="s2">&quot;testGroupIndex/accessGroupAccessGroup&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;975ecf5a45e3bcb680dba0722a420ad9&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging group&quot;</span><span class="p">,</span>
    <span class="n">include</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;emails&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">requires</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;ips&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;office_ip&quot;</span><span class="p">]],</span>
    <span class="p">})</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">require</span></code>, <code class="docutils literal notranslate"><span class="pre">exclude</span></code> and <code class="docutils literal notranslate"><span class="pre">include</span></code> arguments share the available
conditions which can be applied. The conditions are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> - (Optional) A list of IP addresses or ranges. Example:
<code class="docutils literal notranslate"><span class="pre">ip</span> <span class="pre">=</span> <span class="pre">[&quot;1.2.3.4&quot;,</span> <span class="pre">&quot;10.0.0.0/2&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> - (Optional) A list of email addresses. Example:
<code class="docutils literal notranslate"><span class="pre">email</span> <span class="pre">=</span> <span class="pre">[&quot;test&#64;example.com&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_domain</span></code> - (Optional) A list of email domains. Example:
<code class="docutils literal notranslate"><span class="pre">email_domain</span> <span class="pre">=</span> <span class="pre">[&quot;example.com&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_token</span></code> - (Optional) A list of service token ids. Example:
<code class="docutils literal notranslate"><span class="pre">service_token</span> <span class="pre">=</span> <span class="pre">[cloudflare_access_service_token.demo.id]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">any_valid_service_token</span></code> - (Optional) Boolean indicating if allow
all tokens to be granted. Example: <code class="docutils literal notranslate"><span class="pre">any_valid_service_token</span> <span class="pre">=</span> <span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> - (Optional) A list of access group ids. Example:
<code class="docutils literal notranslate"><span class="pre">group</span> <span class="pre">=</span> <span class="pre">[cloudflare_access_group.demo.id]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> - (Optional) Boolean indicating permitting access for all
requests. Example: <code class="docutils literal notranslate"><span class="pre">everyone</span> <span class="pre">=</span> <span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> - (Optional) Whether to use mTLS certificate authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">common_name</span></code> - (Optional) Use a certificate common name to authenticate with.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuite</span></code> - (Optional) Use GSuite as the authentication mechanism. Example:</p>
<div class="highlight-hcl notranslate"><div class="highlight"><pre><span></span># ... other configuration
include {
  gsuite {
    email = &quot;admins@example.com&quot;
    identity_provider_id = &quot;ca298b82-93b5-41bf-bc2d-10493f09b761&quot;
  }
}
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">github</span></code> - (Optional) Use a GitHub team as the <code class="docutils literal notranslate"><span class="pre">include</span></code> condition. Example:</p>
<div class="highlight-hcl notranslate"><div class="highlight"><pre><span></span># ... other configuration
include {
  github {
    name = &quot;my-github-team-name&quot;
    identity_provider_id = &quot;ca298b82-93b5-41bf-bc2d-10493f09b761&quot;
  }
}
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">azure</span></code> - (Optional) Use Azure AD as the <code class="docutils literal notranslate"><span class="pre">include</span></code> condition. Example:</p>
<div class="highlight-hcl notranslate"><div class="highlight"><pre><span></span># ... other configuration
include {
  azure {
    id = &quot;86773093-5feb-48dd-814b-7ccd3676ff50e&quot;
    identity_provider_id = &quot;ca298b82-93b5-41bf-bc2d-10493f09b761&quot;
  }
}
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">okta</span></code> - (Optional) Use Okta as the <code class="docutils literal notranslate"><span class="pre">include</span></code> condition. Example:</p>
<div class="highlight-hcl notranslate"><div class="highlight"><pre><span></span># ... other configuration
include {
  okta {
    name = &quot;admins&quot;
    identity_provider_id = &quot;ca298b82-93b5-41bf-bc2d-10493f09b761&quot;
  }
}
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">saml</span></code> - (Optional) Use an external SAML setup as the <code class="docutils literal notranslate"><span class="pre">include</span></code> condition.
Example:</p>
<div class="highlight-hcl notranslate"><div class="highlight"><pre><span></span># ... other configuration
include {
  saml {
    attribute_name = &quot;group&quot;
    attribute_value = &quot;admins&quot;
    identity_provider_id = &quot;ca298b82-93b5-41bf-bc2d-10493f09b761&quot;
  }
}
</pre></div>
</div>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account the group is
associated with.</p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Group.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>requires</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessGroup.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the account the group is
associated with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessGroup.excludes">
<code class="sig-name descname">excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessGroup.includes">
<code class="sig-name descname">includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.includes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessGroup.requires">
<code class="sig-name descname">requires</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.requires" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requires</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account the group is
associated with.</p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Group.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>requires</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessIdentityProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessIdentityProvider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Identity Provider resource. Identity Providers are
used as an authentication or authorisation source within Access.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># one time pin</span>
<span class="n">pin_login</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessIdentityProvider</span><span class="p">(</span><span class="s2">&quot;pinLogin&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;PIN login&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;onetimepin&quot;</span><span class="p">)</span>
<span class="c1"># oauth</span>
<span class="n">github_oauth</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessIdentityProvider</span><span class="p">(</span><span class="s2">&quot;githubOauth&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">,</span>
    <span class="n">configs</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;clientId&quot;</span><span class="p">:</span> <span class="s2">&quot;example&quot;</span><span class="p">,</span>
        <span class="s2">&quot;clientSecret&quot;</span><span class="p">:</span> <span class="s2">&quot;secret_key&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;GitHub OAuth&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;github&quot;</span><span class="p">)</span>
<span class="c1"># saml</span>
<span class="n">jumpcloud_saml</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessIdentityProvider</span><span class="p">(</span><span class="s2">&quot;jumpcloudSaml&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span><span class="p">,</span>
    <span class="n">configs</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;attributes&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;email&quot;</span><span class="p">,</span>
            <span class="s2">&quot;username&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;idpPublicCert&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;&quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQ...GF/Q2/MHadws97cZg</span>
<span class="s2">uTnQyuOqPuHbnN83d/2l1NSYKCbHt24o</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;issuerUrl&quot;</span><span class="p">:</span> <span class="s2">&quot;jumpcloud&quot;</span><span class="p">,</span>
        <span class="s2">&quot;signRequest&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;ssoTargetUrl&quot;</span><span class="p">:</span> <span class="s2">&quot;https://sso.myexample.jumpcloud.com/saml2/cloudflareaccess&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;JumpCloud SAML&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;saml&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Provider configuration from the [developer documentation][access_identity_provider_guide].</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Identity Provider configuration.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appsDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certsUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">directoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailAttributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpPublicCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktaAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneloginAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoTargetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessIdentityProvider.configs">
<code class="sig-name descname">configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.configs" title="Permalink to this definition">¶</a></dt>
<dd><p>Provider configuration from the [developer documentation][access_identity_provider_guide].</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appsDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certsUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">directoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailAttributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpPublicCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktaAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneloginAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoTargetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessIdentityProvider.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Identity Provider configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessIdentityProvider.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessIdentityProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Provider configuration from the [developer documentation][access_identity_provider_guide].</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Identity Provider configuration.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appsDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certsUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">directoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailAttributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpPublicCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktaAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneloginAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoTargetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessIdentityProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">decision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">precedence</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requires</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Policy resource. Access Policies are used
in conjunction with Access Applications to restrict access to a
particular resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Allowing access to `test@example.com` email address only</span>
<span class="n">test_policy_access_policy</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessPolicy</span><span class="p">(</span><span class="s2">&quot;testPolicyAccessPolicy&quot;</span><span class="p">,</span>
    <span class="n">application_id</span><span class="o">=</span><span class="s2">&quot;cb029e245cfdd66dc8d2e570d5dd3322&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging policy&quot;</span><span class="p">,</span>
    <span class="n">precedence</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="n">decision</span><span class="o">=</span><span class="s2">&quot;allow&quot;</span><span class="p">,</span>
    <span class="n">include</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;emails&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">],</span>
    <span class="p">}])</span>
<span class="c1"># Allowing `test@example.com` to access but only when coming from a</span>
<span class="c1"># specific IP.</span>
<span class="n">test_policy_index_access_policy_access_policy</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessPolicy</span><span class="p">(</span><span class="s2">&quot;testPolicyIndex/accessPolicyAccessPolicy&quot;</span><span class="p">,</span>
    <span class="n">application_id</span><span class="o">=</span><span class="s2">&quot;cb029e245cfdd66dc8d2e570d5dd3322&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;staging policy&quot;</span><span class="p">,</span>
    <span class="n">precedence</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="n">decision</span><span class="o">=</span><span class="s2">&quot;allow&quot;</span><span class="p">,</span>
    <span class="n">include</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;emails&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">requires</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;ips&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;office_ip&quot;</span><span class="p">]],</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application the policy is
associated with.</p></li>
<li><p><strong>decision</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">non_identity</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The unique precedence for policies on a single application. Integer.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be
added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>requires</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessPolicy.application_id">
<code class="sig-name descname">application_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application the policy is
associated with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessPolicy.decision">
<code class="sig-name descname">decision</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.decision" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">non_identity</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessPolicy.excludes">
<code class="sig-name descname">excludes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessPolicy.includes">
<code class="sig-name descname">includes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.includes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessPolicy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessPolicy.precedence">
<code class="sig-name descname">precedence</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.precedence" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique precedence for policies on a single application. Integer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessPolicy.requires">
<code class="sig-name descname">requires</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.requires" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessPolicy.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be
added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">decision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excludes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">includes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">precedence</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requires</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application the policy is
associated with.</p></li>
<li><p><strong>decision</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">non_identity</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The unique precedence for policies on a single application. Integer.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A series of access conditions, see <a class="reference external" href="https://www.terraform.io/docs/providers/cloudflare/r/access_group.html#conditions">Access Groups</a>.</p>
</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be
added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>requires</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">anyValidServiceToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">githubs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gsuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Friendly name of the Access Application.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">samls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributeValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identityProviderId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceTokens</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare IP Firewall Access Rule resource. Access control can be applied on basis of IP addresses, IP ranges, AS numbers or countries.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rule configuration to apply to a matched request. It’s a complex value. See description below.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A personal note about the rule. Typically used as a reminder or explanation for the rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request property to target. Allowed values: “ip”, “ip6”, “ip_range”, “asn”, “country”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to target. Depends on target’s type.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessRule.configuration">
<code class="sig-name descname">configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Rule configuration to apply to a matched request. It’s a complex value. See description below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The request property to target. Allowed values: “ip”, “ip6”, “ip_range”, “asn”, “country”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to target. Depends on target’s type.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessRule.mode">
<code class="sig-name descname">mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessRule.notes">
<code class="sig-name descname">notes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>A personal note about the rule. Typically used as a reminder or explanation for the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessRule.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rule configuration to apply to a matched request. It’s a complex value. See description below.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A personal note about the rule. Typically used as a reminder or explanation for the rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request property to target. Allowed values: “ip”, “ip6”, “ip_range”, “asn”, “country”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to target. Depends on target’s type.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessServiceToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessServiceToken</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken" title="Permalink to this definition">¶</a></dt>
<dd><p>Access Service Tokens are used for service-to-service communication
when an application is behind Cloudflare Access.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">my_app</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccessServiceToken</span><span class="p">(</span><span class="s2">&quot;myApp&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;CI/CD app&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account where the Access
Service is being created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the token’s intent.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessServiceToken.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the account where the Access
Service is being created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessServiceToken.client_id">
<code class="sig-name descname">client_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>UUID client ID associated with the Service Token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessServiceToken.client_secret">
<code class="sig-name descname">client_secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>A secret for interacting with Access protocols.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccessServiceToken.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the token’s intent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessServiceToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account where the Access
Service is being created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UUID client ID associated with the Service Token.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A secret for interacting with Access protocols.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the token’s intent.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccessServiceToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessServiceToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccountMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccountMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare account members.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example_user</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">AccountMember</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">email_address</span><span class="o">=</span><span class="s2">&quot;user@example.com&quot;</span><span class="p">,</span>
    <span class="n">role_ids</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;68b329da9893e34099c7d8ad5cb9c940&quot;</span><span class="p">,</span>
        <span class="s2">&quot;d784fa8b6d98d27699781bd9a7cf19f0&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of account role IDs that you want to assign to a member.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.AccountMember.email_address">
<code class="sig-name descname">email_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccountMember.email_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.AccountMember.role_ids">
<code class="sig-name descname">role_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccountMember.role_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of account role IDs that you want to assign to a member.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccountMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of account role IDs that you want to assign to a member.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.AccountMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccountMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Argo">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Argo</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smart_routing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tiered_caching</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloudflare Argo controls the routing to your origin and tiered caching options to speed up your website browsing experience.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Argo</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">smart_routing</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
    <span class="n">tiered_caching</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tiered_caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID that you wish to manage Argo on.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.Argo.smart_routing">
<code class="sig-name descname">smart_routing</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.smart_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Argo.tiered_caching">
<code class="sig-name descname">tiered_caching</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.tiered_caching" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Argo.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID that you wish to manage Argo on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Argo.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smart_routing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tiered_caching</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Argo resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tiered_caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID that you wish to manage Argo on.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Argo.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Argo.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AwaitableGetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetWafGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetWafPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafPackagesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetWafRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.CustomPages">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CustomPages</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare custom error pages.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">basic_challenge</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">CustomPages</span><span class="p">(</span><span class="s2">&quot;basicChallenge&quot;</span><span class="p">,</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;customized&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;basic_challenge&quot;</span><span class="p">,</span>
    <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://example.com/challenge.html&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of where the custom page source is located.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.CustomPages.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.CustomPages.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.CustomPages.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of where the custom page source is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.CustomPages.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomPages.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomPages resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of where the custom page source is located.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomPages.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomPages.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomSsl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CustomSsl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ssl_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ssl_priorities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare custom ssl resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">cloudflare_zone_id</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;cloudflareZoneId&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">cloudflare_zone_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">cloudflare_zone_id</span> <span class="o">=</span> <span class="s2">&quot;1d5fdc9e88c8a8c4518b068cd94331fe&quot;</span>
<span class="c1"># Add a custom ssl certificate to the domain</span>
<span class="n">foossl</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">CustomSsl</span><span class="p">(</span><span class="s2">&quot;foossl&quot;</span><span class="p">,</span>
    <span class="n">custom_ssl_options</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;bundle_method&quot;</span><span class="p">:</span> <span class="s2">&quot;ubiquitous&quot;</span><span class="p">,</span>
        <span class="s2">&quot;certificate&quot;</span><span class="p">:</span> <span class="s2">&quot;-----INSERT CERTIFICATE-----&quot;</span><span class="p">,</span>
        <span class="s2">&quot;geo_restrictions&quot;</span><span class="p">:</span> <span class="s2">&quot;us&quot;</span><span class="p">,</span>
        <span class="s2">&quot;private_key&quot;</span><span class="p">:</span> <span class="s2">&quot;-----INSERT PRIVATE KEY-----&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;legacy_custom&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">cloudflare_zone_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_ssl_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone id to the custom ssl cert should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_ssl_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bundle_method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Method of building intermediate certificate chain. A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Valid values are <code class="docutils literal notranslate"><span class="pre">ubiquitous</span></code> (default), <code class="docutils literal notranslate"><span class="pre">optimal</span></code>, <code class="docutils literal notranslate"><span class="pre">force</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate certificate and the intermediate(s)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geo_restrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the region where your private key can be held locally. Valid values are <code class="docutils literal notranslate"><span class="pre">us</span></code>, <code class="docutils literal notranslate"><span class="pre">eu</span></code>, <code class="docutils literal notranslate"><span class="pre">highest_security</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate’s private key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to enable support for legacy clients which do not include SNI in the TLS handshake. Valid values are <code class="docutils literal notranslate"><span class="pre">legacy_custom</span></code> (default), <code class="docutils literal notranslate"><span class="pre">sni_custom</span></code>.</p></li>
</ul>
<p>The <strong>custom_ssl_priorities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.CustomSsl.custom_ssl_options">
<code class="sig-name descname">custom_ssl_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.custom_ssl_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bundle_method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Method of building intermediate certificate chain. A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Valid values are <code class="docutils literal notranslate"><span class="pre">ubiquitous</span></code> (default), <code class="docutils literal notranslate"><span class="pre">optimal</span></code>, <code class="docutils literal notranslate"><span class="pre">force</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Certificate certificate and the intermediate(s)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geo_restrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the region where your private key can be held locally. Valid values are <code class="docutils literal notranslate"><span class="pre">us</span></code>, <code class="docutils literal notranslate"><span class="pre">eu</span></code>, <code class="docutils literal notranslate"><span class="pre">highest_security</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Certificate’s private key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to enable support for legacy clients which do not include SNI in the TLS handshake. Valid values are <code class="docutils literal notranslate"><span class="pre">legacy_custom</span></code> (default), <code class="docutils literal notranslate"><span class="pre">sni_custom</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.CustomSsl.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone id to the custom ssl cert should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomSsl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ssl_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ssl_priorities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signature</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uploaded_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomSsl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_ssl_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone id to the custom ssl cert should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_ssl_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bundle_method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Method of building intermediate certificate chain. A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Valid values are <code class="docutils literal notranslate"><span class="pre">ubiquitous</span></code> (default), <code class="docutils literal notranslate"><span class="pre">optimal</span></code>, <code class="docutils literal notranslate"><span class="pre">force</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate certificate and the intermediate(s)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geo_restrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the region where your private key can be held locally. Valid values are <code class="docutils literal notranslate"><span class="pre">us</span></code>, <code class="docutils literal notranslate"><span class="pre">eu</span></code>, <code class="docutils literal notranslate"><span class="pre">highest_security</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate’s private key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to enable support for legacy clients which do not include SNI in the TLS handshake. Valid values are <code class="docutils literal notranslate"><span class="pre">legacy_custom</span></code> (default), <code class="docutils literal notranslate"><span class="pre">sni_custom</span></code>.</p></li>
</ul>
<p>The <strong>custom_ssl_priorities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.CustomSsl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomSsl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Filter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Filter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Filter expressions that can be referenced across multiple features, e.g. Firewall Rule. The expression format is similar to <a class="reference external" href="https://www.wireshark.org/docs/man-pages/wireshark-filter.html">Wireshark Display Filter</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">wordpress</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Filter</span><span class="p">(</span><span class="s2">&quot;wordpress&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Wordpress break-in attempts that are outside of the office&quot;</span><span class="p">,</span>
    <span class="n">expression</span><span class="o">=</span><span class="s2">&quot;(http.request.uri.path ~ &quot;</span><span class="o">.*</span><span class="n">wp</span><span class="o">-</span><span class="n">login</span><span class="o">.</span><span class="n">php</span><span class="s2">&quot; or http.request.uri.path ~ &quot;</span><span class="o">.*</span><span class="n">xmlrpc</span><span class="o">.</span><span class="n">php</span><span class="s2">&quot;) and ip.src ne 192.0.2.1&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the purpose of the filter.</p></li>
<li><p><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter expression to be used.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter is currently paused. Boolean value.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short reference tag to quickly select related rules.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.Filter.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that you can use to describe the purpose of the filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Filter.expression">
<code class="sig-name descname">expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter expression to be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Filter.paused">
<code class="sig-name descname">paused</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this filter is currently paused. Boolean value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Filter.ref">
<code class="sig-name descname">ref</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.ref" title="Permalink to this definition">¶</a></dt>
<dd><p>Short reference tag to quickly select related rules.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Filter.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Filter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Filter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the purpose of the filter.</p></li>
<li><p><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter expression to be used.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter is currently paused. Boolean value.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short reference tag to quickly select related rules.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Filter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Filter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Define Firewall rules using filter expressions for more control over how traffic is matched to the rule.
A filter expression permits selecting traffic by multiple criteria allowing greater freedom in rule creation.</p>
<p>Filter expressions needs to be created first before using Firewall Rule. See Filter.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">wordpress_filter</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Filter</span><span class="p">(</span><span class="s2">&quot;wordpressFilter&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Wordpress break-in attempts that are outside of the office&quot;</span><span class="p">,</span>
    <span class="n">expression</span><span class="o">=</span><span class="s2">&quot;(http.request.uri.path ~ &quot;</span><span class="o">.*</span><span class="n">wp</span><span class="o">-</span><span class="n">login</span><span class="o">.</span><span class="n">php</span><span class="s2">&quot; or http.request.uri.path ~ &quot;</span><span class="o">.*</span><span class="n">xmlrpc</span><span class="o">.</span><span class="n">php</span><span class="s2">&quot;) and ip.src ne 192.0.2.1&quot;</span><span class="p">)</span>
<span class="n">wordpress_firewall_rule</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">FirewallRule</span><span class="p">(</span><span class="s2">&quot;wordpressFirewallRule&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Block wordpress break-in attempts&quot;</span><span class="p">,</span>
    <span class="n">filter_id</span><span class="o">=</span><span class="n">wordpress_filter</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">action</span><span class="o">=</span><span class="s2">&quot;block&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule to help identify it.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter based firewall rule is currently paused. Boolean value.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p></li>
<li><p><strong>products</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.FirewallRule.action">
<code class="sig-name descname">action</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.FirewallRule.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the rule to help identify it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.FirewallRule.paused">
<code class="sig-name descname">paused</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this filter based firewall rule is currently paused. Boolean value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.FirewallRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.FirewallRule.products">
<code class="sig-name descname">products</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.products" title="Permalink to this definition">¶</a></dt>
<dd><p>List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.FirewallRule.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule to help identify it.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter based firewall rule is currently paused. Boolean value.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p></li>
<li><p><strong>products</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.GetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpRanges.</p>
<dl class="py attribute">
<dt id="pulumi_cloudflare.GetIpRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetWafGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafGroups.</p>
<dl class="py attribute">
<dt id="pulumi_cloudflare.GetWafGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetWafGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetWafPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafPackagesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">packages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafPackages.</p>
<dl class="py attribute">
<dt id="pulumi_cloudflare.GetWafPackagesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetWafPackagesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetWafRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafRules.</p>
<dl class="py attribute">
<dt id="pulumi_cloudflare.GetWafRulesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetWafRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py attribute">
<dt id="pulumi_cloudflare.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudflare.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_pool_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pop_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxied</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_affinity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steering_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Load Balancer resource. This sits in front of a number of defined pools of origins and provides various options for geographically-aware load balancing. Note that the load balancing feature must be enabled in your Cloudflare account before you can use this resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerPool</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-lb-pool&quot;</span><span class="p">,</span>
    <span class="n">origins</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;example-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;192.0.2.1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">}])</span>
<span class="c1"># Define a load balancer which always points to a pool we define below</span>
<span class="c1"># In normal usage, would have different pools set for different pops (cloudflare points-of-presence) and/or for different regions</span>
<span class="c1"># Within each pop or region we can define multiple pools in failover order</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-load-balancer&quot;</span><span class="p">,</span>
    <span class="n">fallback_pool_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">default_pool_ids</span><span class="o">=</span><span class="p">[</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example load balancer using geo-balancing&quot;</span><span class="p">,</span>
    <span class="n">proxied</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">steering_policy</span><span class="o">=</span><span class="s2">&quot;geo&quot;</span><span class="p">,</span>
    <span class="n">pop_pools</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;pop&quot;</span><span class="p">:</span> <span class="s2">&quot;LAX&quot;</span><span class="p">,</span>
        <span class="s2">&quot;poolIds&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">region_pools</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;region&quot;</span><span class="p">:</span> <span class="s2">&quot;WNAM&quot;</span><span class="p">,</span>
        <span class="s2">&quot;poolIds&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_pool_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p></li>
<li><p><strong>fallback_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pool ID to use when all other pools are detected as unhealthy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name (FQDN, including the zone) to associate with the load balancer.</p></li>
<li><p><strong>pop_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>region_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p></li>
<li><p><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>steering_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the load balancer to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>pop_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A 3-letter code for the Point-of-Presence. Allowed values can be found in the list of datacenters on the <a class="reference external" href="https://www.cloudflarestatus.com/">status page</a>. Multiple entries should not be specified with the same PoP.</p></li>
</ul>
<p>The <strong>region_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A region code which must be in the list defined <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>. Multiple entries should not be specified with the same region.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.created_on">
<code class="sig-name descname">created_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.default_pool_ids">
<code class="sig-name descname">default_pool_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.default_pool_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.fallback_pool_id">
<code class="sig-name descname">fallback_pool_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.fallback_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The pool ID to use when all other pools are detected as unhealthy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.modified_on">
<code class="sig-name descname">modified_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was last modified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name (FQDN, including the zone) to associate with the load balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.pop_pools">
<code class="sig-name descname">pop_pools</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.pop_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pop</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A 3-letter code for the Point-of-Presence. Allowed values can be found in the list of datacenters on the <a class="reference external" href="https://www.cloudflarestatus.com/">status page</a>. Multiple entries should not be specified with the same PoP.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.proxied">
<code class="sig-name descname">proxied</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.proxied" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.region_pools">
<code class="sig-name descname">region_pools</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.region_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A region code which must be in the list defined <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>. Multiple entries should not be specified with the same region.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.session_affinity">
<code class="sig-name descname">session_affinity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.steering_policy">
<code class="sig-name descname">steering_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.steering_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancer.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to add the load balancer to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_pool_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pop_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxied</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_affinity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steering_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was created.</p></li>
<li><p><strong>default_pool_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p></li>
<li><p><strong>fallback_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pool ID to use when all other pools are detected as unhealthy.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was last modified.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name (FQDN, including the zone) to associate with the load balancer.</p></li>
<li><p><strong>pop_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>region_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p></li>
<li><p><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>steering_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the load balancer to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>pop_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A 3-letter code for the Point-of-Presence. Allowed values can be found in the list of datacenters on the <a class="reference external" href="https://www.cloudflarestatus.com/">status page</a>. Multiple entries should not be specified with the same PoP.</p></li>
</ul>
<p>The <strong>region_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A region code which must be in the list defined <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>. Multiple entries should not be specified with the same region.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerMonitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancerMonitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_insecure</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">follow_redirects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor" title="Permalink to this definition">¶</a></dt>
<dd><p>If you’re using Cloudflare’s Load Balancing to load-balance across multiple origin servers or data centers, you configure one of these Monitors to actively check the availability of those servers over HTTP(S) or TCP.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">http_monitor</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerMonitor</span><span class="p">(</span><span class="s2">&quot;httpMonitor&quot;</span><span class="p">,</span>
    <span class="n">allow_insecure</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example http load balancer&quot;</span><span class="p">,</span>
    <span class="n">expected_body</span><span class="o">=</span><span class="s2">&quot;alive&quot;</span><span class="p">,</span>
    <span class="n">expected_codes</span><span class="o">=</span><span class="s2">&quot;2xx&quot;</span><span class="p">,</span>
    <span class="n">follow_redirects</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">headers</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;header&quot;</span><span class="p">:</span> <span class="s2">&quot;Host&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;example.com&quot;</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/health&quot;</span><span class="p">,</span>
    <span class="n">retries</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">timeout</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">tcp_monitor</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerMonitor</span><span class="p">(</span><span class="s2">&quot;tcpMonitor&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example tcp load balancer&quot;</span><span class="p">,</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;connection_established&quot;</span><span class="p">,</span>
    <span class="n">retries</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">timeout</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;tcp&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The header name.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. Default: 5.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of string values for the header.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.allow_insecure">
<code class="sig-name descname">allow_insecure</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.allow_insecure" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.created_on">
<code class="sig-name descname">created_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer monitor was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.expected_body">
<code class="sig-name descname">expected_body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.expected_body" title="Permalink to this definition">¶</a></dt>
<dd><p>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.expected_codes">
<code class="sig-name descname">expected_codes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.expected_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.follow_redirects">
<code class="sig-name descname">follow_redirects</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.follow_redirects" title="Permalink to this definition">¶</a></dt>
<dd><p>Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.headers">
<code class="sig-name descname">headers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>The header name.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of string values for the header.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.interval">
<code class="sig-name descname">interval</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.method">
<code class="sig-name descname">method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.modified_on">
<code class="sig-name descname">modified_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer monitor was last modified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.path">
<code class="sig-name descname">path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.retries">
<code class="sig-name descname">retries</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.retries" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout (in seconds) before marking the health check as failed. Default: 5.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_insecure</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">follow_redirects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerMonitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer monitor was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The header name.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer monitor was last modified.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. Default: 5.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of string values for the header.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerMonitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancerPool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Load Balancer pool resource. This provides a pool of origins that can be used by a Cloudflare Load Balancer. Note that the load balancing feature must be enabled in your Cloudflare account before you can use this resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LoadBalancerPool</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example load balancer pool&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">minimum_origins</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-pool&quot;</span><span class="p">,</span>
    <span class="n">notification_email</span><span class="o">=</span><span class="s2">&quot;someone@example.com&quot;</span><span class="p">,</span>
    <span class="n">origins</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;192.0.2.1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;example-1&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;192.0.2.2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;example-2&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><strong>minimum_origins</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p></li>
<li><p><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Monitor to use for health checking origins within this pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-identifiable name for the origin.</p></li>
<li><p><strong>notification_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to send health status notifications to. This can be an individual mailbox or a mailing list.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address (IPv4 or IPv6) of the origin, or the publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A human-identifiable name for the origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The weight (0.01 - 1.00) of this origin, relative to other origins in the pool. Equal values mean equal weighting. A weight of 0 means traffic will not be sent to this origin, but health is still checked. Default: 1.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.check_regions">
<code class="sig-name descname">check_regions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.check_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.created_on">
<code class="sig-name descname">created_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.minimum_origins">
<code class="sig-name descname">minimum_origins</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.minimum_origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.modified_on">
<code class="sig-name descname">modified_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was last modified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.monitor">
<code class="sig-name descname">monitor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Monitor to use for health checking origins within this pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-identifiable name for the origin.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.notification_email">
<code class="sig-name descname">notification_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.notification_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address to send health status notifications to. This can be an individual mailbox or a mailing list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.origins">
<code class="sig-name descname">origins</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address (IPv4 or IPv6) of the origin, or the publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A human-identifiable name for the origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The weight (0.01 - 1.00) of this origin, relative to other origins in the pool. Equal values mean equal weighting. A weight of 0 means traffic will not be sent to this origin, but health is still checked. Default: 1.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><strong>minimum_origins</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was last modified.</p></li>
<li><p><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Monitor to use for health checking origins within this pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-identifiable name for the origin.</p></li>
<li><p><strong>notification_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to send health status notifications to. This can be an individual mailbox or a mailing list.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address (IPv4 or IPv6) of the origin, or the publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A human-identifiable name for the origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The weight (0.01 - 1.00) of this origin, relative to other origins in the pool. Equal values mean equal weighting. A weight of 0 means traffic will not be sent to this origin, but health is still checked. Default: 1.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LoadBalancerPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpushJob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LogpushJob</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_conf</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logpull_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ownership_challenge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare logpush jobs.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example_job</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">LogpushJob</span><span class="p">(</span><span class="s2">&quot;exampleJob&quot;</span><span class="p">,</span>
    <span class="n">dataset</span><span class="o">=</span><span class="s2">&quot;http_requests&quot;</span><span class="p">,</span>
    <span class="n">destination_conf</span><span class="o">=</span><span class="s2">&quot;s3://my-bucket-path?region=us-west-2&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">logpull_options</span><span class="o">=</span><span class="s2">&quot;fields=RayID,ClientIP,EdgeStartTimestamp&amp;timestamps=rfc3339&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;My-logpush-job&quot;</span><span class="p">,</span>
    <span class="n">ownership_challenge</span><span class="o">=</span><span class="s2">&quot;00000000000000000&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which type of dataset resource to use. Available values are <code class="docutils literal notranslate"><span class="pre">&quot;firewall_events&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http_requests&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;spectrum_events&quot;</span></code>.</p></li>
<li><p><strong>destination_conf</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p></li>
<li><p><strong>logpull_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.</p></li>
<li><p><strong>ownership_challenge</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the logpush job should be created.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.LogpushJob.dataset">
<code class="sig-name descname">dataset</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>Which type of dataset resource to use. Available values are <code class="docutils literal notranslate"><span class="pre">&quot;firewall_events&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http_requests&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;spectrum_events&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LogpushJob.destination_conf">
<code class="sig-name descname">destination_conf</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.destination_conf" title="Permalink to this definition">¶</a></dt>
<dd><p>Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LogpushJob.logpull_options">
<code class="sig-name descname">logpull_options</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.logpull_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LogpushJob.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LogpushJob.ownership_challenge">
<code class="sig-name descname">ownership_challenge</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.ownership_challenge" title="Permalink to this definition">¶</a></dt>
<dd><p>Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.LogpushJob.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID where the logpush job should be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_conf</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logpull_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ownership_challenge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogpushJob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which type of dataset resource to use. Available values are <code class="docutils literal notranslate"><span class="pre">&quot;firewall_events&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;http_requests&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;spectrum_events&quot;</span></code>.</p></li>
<li><p><strong>destination_conf</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p>
</p></li>
<li><p><strong>logpull_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.</p></li>
<li><p><strong>ownership_challenge</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.</p>
</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the logpush job should be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.LogpushJob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpushJob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.OriginCaCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">OriginCaCertificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_validity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Origin CA certificate used to protect traffic to your origin without involving a third party Certificate Authority.</p>
<p><strong>This resource requires you use your Origin CA Key as the ``api_user_service_key``.</strong></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Signing Request. Must be newline-encoded.</p></li>
<li><p><strong>hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of hostnames or wildcard names bound to the certificate.</p></li>
<li><p><strong>request_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The signature type desired on the certificate.</p></li>
<li><p><strong>requested_validity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days for which the certificate should be valid.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.certificate">
<code class="sig-name descname">certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The Origin CA certificate</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.csr">
<code class="sig-name descname">csr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Signing Request. Must be newline-encoded.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.expires_on">
<code class="sig-name descname">expires_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.expires_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The datetime when the certificate will expire.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.hostnames">
<code class="sig-name descname">hostnames</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of hostnames or wildcard names bound to the certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.request_type">
<code class="sig-name descname">request_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.request_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The signature type desired on the certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.requested_validity">
<code class="sig-name descname">requested_validity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.requested_validity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days for which the certificate should be valid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">csr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_validity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OriginCaCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Origin CA certificate</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Signing Request. Must be newline-encoded.</p></li>
<li><p><strong>expires_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datetime when the certificate will expire.</p></li>
<li><p><strong>hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of hostnames or wildcard names bound to the certificate.</p></li>
<li><p><strong>request_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The signature type desired on the certificate.</p></li>
<li><p><strong>requested_validity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days for which the certificate should be valid.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.OriginCaCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.OriginCaCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.PageRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">PageRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare page rule resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Add a page rule to the domain</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">PageRule</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">target</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;sub.</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;cloudflare_zone&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/page&quot;</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">actions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;ssl&quot;</span><span class="p">:</span> <span class="s2">&quot;flexible&quot;</span><span class="p">,</span>
        <span class="s2">&quot;emailObfuscation&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="s2">&quot;minify&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;html&quot;</span><span class="p">:</span> <span class="s2">&quot;off&quot;</span><span class="p">,</span>
            <span class="s2">&quot;css&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
            <span class="s2">&quot;js&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="p">}],</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The actions taken by the page rule, options given below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the page rule is active or disabled.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL pattern to target with the page rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the page rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Time To Live for the browser cache. <code class="docutils literal notranslate"><span class="pre">0</span></code> means ‘Respect Existing Headers’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassCacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value of cookie name to conditionally bypass cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheByDeviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDeceptionArmor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the cache level to <code class="docutils literal notranslate"><span class="pre">&quot;bypass&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;simplified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aggressive&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;cache_everything&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value of cookie name to conditionally cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableApps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disablePerformance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableRailgun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Time To Live for the edge cache.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">explicitCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether origin Cache-Control action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The URL to forward to, and with what status. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code to use for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to which the page rule should forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeaderOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the Host header to send.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minifies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The configuration for HTML, CSS and JS minification. See below for full list of options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether CSS should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether HTML should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether Javascript should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;lossless&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;lossy&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolveOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overridden origin server name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">respectStrongEtag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the rocket loader to <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the security level to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;essentially_off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;medium&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;under_attack&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the SSL mode to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;flexible&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;full&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;strict&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;origin_pull&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.PageRule.actions">
<code class="sig-name descname">actions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>The actions taken by the page rule, options given below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Time To Live for the browser cache. <code class="docutils literal notranslate"><span class="pre">0</span></code> means ‘Respect Existing Headers’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassCacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String value of cookie name to conditionally bypass cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheByDeviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDeceptionArmor</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to set the cache level to <code class="docutils literal notranslate"><span class="pre">&quot;bypass&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;simplified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aggressive&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;cache_everything&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String value of cookie name to conditionally cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableApps</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disablePerformance</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableRailgun</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Time To Live for the edge cache.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">explicitCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether origin Cache-Control action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The URL to forward to, and with what status. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The status code to use for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL to which the page rule should forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeaderOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the Host header to send.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minifies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The configuration for HTML, CSS and JS minification. See below for full list of options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether CSS should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether HTML should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether Javascript should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;lossless&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;lossy&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolveOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Overridden origin server name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">respectStrongEtag</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to set the rocket loader to <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to set the security level to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;essentially_off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;medium&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;under_attack&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to set the SSL mode to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;flexible&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;full&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;strict&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;origin_pull&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.PageRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.PageRule.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the page rule is active or disabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.PageRule.target">
<code class="sig-name descname">target</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL pattern to target with the page rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.PageRule.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which the page rule should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PageRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The actions taken by the page rule, options given below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p>
</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the page rule is active or disabled.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL pattern to target with the page rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the page rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Time To Live for the browser cache. <code class="docutils literal notranslate"><span class="pre">0</span></code> means ‘Respect Existing Headers’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassCacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value of cookie name to conditionally bypass cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheByDeviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDeceptionArmor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the cache level to <code class="docutils literal notranslate"><span class="pre">&quot;bypass&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;simplified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aggressive&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;cache_everything&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value of cookie name to conditionally cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableApps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disablePerformance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableRailgun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Time To Live for the edge cache.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">explicitCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether origin Cache-Control action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The URL to forward to, and with what status. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code to use for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to which the page rule should forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeaderOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the Host header to send.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minifies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The configuration for HTML, CSS and JS minification. See below for full list of options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether CSS should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether HTML should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether Javascript should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;lossless&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;lossy&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolveOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overridden origin server name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">respectStrongEtag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the rocket loader to <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the security level to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;essentially_off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;medium&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;under_attack&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the SSL mode to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;flexible&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;full&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;strict&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;origin_pull&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.PageRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.PageRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_client_logging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_user_service_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_backoff</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_backoff</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the cloudflare package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configure API client to always use that account.</p></li>
<li><p><strong>api_client_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to print logs from the API client (using the default log library logger)</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key for operations.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API Token for operations.</p></li>
<li><p><strong>api_user_service_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A special Cloudflare API key good for a restricted set of endpoints.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A registered Cloudflare email address.</p></li>
<li><p><strong>max_backoff</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum backoff period in seconds after failed API calls</p></li>
<li><p><strong>min_backoff</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum backoff period in seconds after failed API calls</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of retries to perform when an API request fails</p></li>
<li><p><strong>rps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – RPS limit to apply when making calls to the API</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudflare.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.RateLimit">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">RateLimit</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bypass_url_patterns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">correlate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare rate limit resource for a given zone. This can be used to limit the traffic you receive zone-wide, or matching more specific types of requests/responses.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">RateLimit</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">threshold</span><span class="o">=</span><span class="mi">2000</span><span class="p">,</span>
    <span class="n">period</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">match</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;request&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;urlPattern&quot;</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;cloudflare_zone&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/*&quot;</span><span class="p">,</span>
            <span class="s2">&quot;schemes&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="s2">&quot;HTTP&quot;</span><span class="p">,</span>
                <span class="s2">&quot;HTTPS&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="s2">&quot;methods&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="s2">&quot;GET&quot;</span><span class="p">,</span>
                <span class="s2">&quot;POST&quot;</span><span class="p">,</span>
                <span class="s2">&quot;PUT&quot;</span><span class="p">,</span>
                <span class="s2">&quot;DELETE&quot;</span><span class="p">,</span>
                <span class="s2">&quot;PATCH&quot;</span><span class="p">,</span>
                <span class="s2">&quot;HEAD&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">},</span>
        <span class="s2">&quot;response&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;statuses&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="mi">200</span><span class="p">,</span>
                <span class="mi">201</span><span class="p">,</span>
                <span class="mi">202</span><span class="p">,</span>
                <span class="mi">301</span><span class="p">,</span>
                <span class="mi">429</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="s2">&quot;originTraffic&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">action</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;mode&quot;</span><span class="p">:</span> <span class="s2">&quot;simulate&quot;</span><span class="p">,</span>
        <span class="s2">&quot;timeout&quot;</span><span class="p">:</span> <span class="mi">43200</span><span class="p">,</span>
        <span class="s2">&quot;response&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;contentType&quot;</span><span class="p">:</span> <span class="s2">&quot;text/plain&quot;</span><span class="p">,</span>
            <span class="s2">&quot;body&quot;</span><span class="p">:</span> <span class="s2">&quot;custom response body&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">correlate</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;by&quot;</span><span class="p">:</span> <span class="s2">&quot;nat&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example rate limit for a zone&quot;</span><span class="p">,</span>
    <span class="n">bypass_url_patterns</span><span class="o">=</span><span class="p">[</span>
        <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;cloudflare_zone&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/bypass1&quot;</span><span class="p">,</span>
        <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">var</span><span class="p">[</span><span class="s1">&#39;cloudflare_zone&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/bypass2&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p></li>
<li><p><strong>bypass_url_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – URLs matching the patterns specified here will be excluded from rate limiting.</p></li>
<li><p><strong>correlate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>match</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply rate limiting to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of action to perform. Allowable values are ‘simulate’, ‘ban’, ‘challenge’ and ‘js_challenge’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The body to return, the content here should conform to the content_type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content-type of the body, must be one of: ‘text/plain’, ‘text/xml’, ‘application/json’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time in seconds as an integer to perform the mitigation action. This field is required if the <code class="docutils literal notranslate"><span class="pre">mode</span></code> is either <code class="docutils literal notranslate"><span class="pre">simulate</span></code> or <code class="docutils literal notranslate"><span class="pre">ban</span></code>. Must be the same or greater than the period (min: 1, max: 86400).</p></li>
</ul>
<p>The <strong>correlate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">by</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If set to ‘nat’, NAT support will be enabled for rate limiting.</p></li>
</ul>
<p>The <strong>match</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Matches HTTP requests (from the client to Cloudflare). See definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Methods, can be a subset [‘POST’,’PUT’] or all [‘_ALL_’]. Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Schemes, can be one [‘HTTPS’], both [‘HTTP’,’HTTPS’] or all [‘_ALL_’].  Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL pattern to match comprised of the host and path, i.e. example.org/path. Wildcard are expanded to match applicable traffic, query strings are not matched. Use * for all traffic to your zone. Default: ‘<a href="#id24"><span class="problematic" id="id25">*</span></a>’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originTraffic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Only count traffic that has come from your origin servers. If true, cached items that Cloudflare serve will not count towards rate limiting. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statuses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Status codes, can be one [403], many [401,403] or indicate all by not providing this value.</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.action">
<code class="sig-name descname">action</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of action to perform. Allowable values are ‘simulate’, ‘ban’, ‘challenge’ and ‘js_challenge’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The body to return, the content here should conform to the content_type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The content-type of the body, must be one of: ‘text/plain’, ‘text/xml’, ‘application/json’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The time in seconds as an integer to perform the mitigation action. This field is required if the <code class="docutils literal notranslate"><span class="pre">mode</span></code> is either <code class="docutils literal notranslate"><span class="pre">simulate</span></code> or <code class="docutils literal notranslate"><span class="pre">ban</span></code>. Must be the same or greater than the period (min: 1, max: 86400).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.bypass_url_patterns">
<code class="sig-name descname">bypass_url_patterns</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.bypass_url_patterns" title="Permalink to this definition">¶</a></dt>
<dd><p>URLs matching the patterns specified here will be excluded from rate limiting.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.correlate">
<code class="sig-name descname">correlate</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.correlate" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">by</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If set to ‘nat’, NAT support will be enabled for rate limiting.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.disabled">
<code class="sig-name descname">disabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.match">
<code class="sig-name descname">match</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.match" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Matches HTTP requests (from the client to Cloudflare). See definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - HTTP Methods, can be a subset [‘POST’,’PUT’] or all [‘_ALL_’]. Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - HTTP Schemes, can be one [‘HTTPS’], both [‘HTTP’,’HTTPS’] or all [‘_ALL_’].  Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL pattern to match comprised of the host and path, i.e. example.org/path. Wildcard are expanded to match applicable traffic, query strings are not matched. Use * for all traffic to your zone. Default: ‘<a href="#id26"><span class="problematic" id="id27">*</span></a>’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originTraffic</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Only count traffic that has come from your origin servers. If true, cached items that Cloudflare serve will not count towards rate limiting. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statuses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - HTTP Status codes, can be one [403], many [401,403] or indicate all by not providing this value.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.threshold">
<code class="sig-name descname">threshold</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.RateLimit.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply rate limiting to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bypass_url_patterns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">correlate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RateLimit resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p></li>
<li><p><strong>bypass_url_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – URLs matching the patterns specified here will be excluded from rate limiting.</p></li>
<li><p><strong>correlate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>match</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply rate limiting to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of action to perform. Allowable values are ‘simulate’, ‘ban’, ‘challenge’ and ‘js_challenge’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The body to return, the content here should conform to the content_type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content-type of the body, must be one of: ‘text/plain’, ‘text/xml’, ‘application/json’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time in seconds as an integer to perform the mitigation action. This field is required if the <code class="docutils literal notranslate"><span class="pre">mode</span></code> is either <code class="docutils literal notranslate"><span class="pre">simulate</span></code> or <code class="docutils literal notranslate"><span class="pre">ban</span></code>. Must be the same or greater than the period (min: 1, max: 86400).</p></li>
</ul>
<p>The <strong>correlate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">by</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If set to ‘nat’, NAT support will be enabled for rate limiting.</p></li>
</ul>
<p>The <strong>match</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Matches HTTP requests (from the client to Cloudflare). See definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Methods, can be a subset [‘POST’,’PUT’] or all [‘_ALL_’]. Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Schemes, can be one [‘HTTPS’], both [‘HTTP’,’HTTPS’] or all [‘_ALL_’].  Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL pattern to match comprised of the host and path, i.e. example.org/path. Wildcard are expanded to match applicable traffic, query strings are not matched. Use * for all traffic to your zone. Default: ‘<a href="#id28"><span class="problematic" id="id29">*</span></a>’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originTraffic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Only count traffic that has come from your origin servers. If true, cached items that Cloudflare serve will not count towards rate limiting. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statuses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Status codes, can be one [403], many [401,403] or indicate all by not providing this value.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.RateLimit.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.RateLimit.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Record">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxied</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Record resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] data: Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified
:param pulumi.Input[str] name: The name of the record
:param pulumi.Input[float] priority: The priority of the record
:param pulumi.Input[bool] proxied: Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[float] ttl: The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)
:param pulumi.Input[str] type: The type of the record
:param pulumi.Input[str] value: The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified
:param pulumi.Input[str] zone_id: The DNS zone ID to add the record to</p>
<p>The <strong>data</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">altitude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fingerprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matching_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_horz</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_vert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proto</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replacement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The type of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.created_on">
<code class="sig-name descname">created_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the record was created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.data">
<code class="sig-name descname">data</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.data" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">altitude</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest_type</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fingerprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_tag</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matching_type</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_horz</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_vert</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preference</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The priority of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proto</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replacement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The type of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the record</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.metadata">
<code class="sig-name descname">metadata</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value map of string metadata Cloudflare associates with the record</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.modified_on">
<code class="sig-name descname">modified_on</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the record was last modified</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the record</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.proxiable">
<code class="sig-name descname">proxiable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.proxiable" title="Permalink to this definition">¶</a></dt>
<dd><p>Shows whether this record can be proxied, must be true if setting <code class="docutils literal notranslate"><span class="pre">proxied=true</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.proxied">
<code class="sig-name descname">proxied</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.proxied" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the record</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Record.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to add the record to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modified_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxiable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxied</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the record was created</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the record</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value map of string metadata Cloudflare associates with the record</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the record was last modified</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the record</p></li>
<li><p><strong>proxiable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Shows whether this record can be proxied, must be true if setting <code class="docutils literal notranslate"><span class="pre">proxied=true</span></code></p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the record to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>data</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">altitude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fingerprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matching_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_horz</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_vert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proto</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replacement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The type of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Record.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Record.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.SpectrumApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">SpectrumApplication</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">argo_smart_routing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_ip_connectivity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_firewall</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_directs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">traffic_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Spectrum Application. You can extend the power of Cloudflare’s DDoS, TLS, and IP Firewall to your other TCP-based services.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Define a spectrum application proxies ssh traffic</span>
<span class="n">ssh_proxy</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">SpectrumApplication</span><span class="p">(</span><span class="s2">&quot;sshProxy&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;tcp/22&quot;</span><span class="p">,</span>
    <span class="n">traffic_type</span><span class="o">=</span><span class="s2">&quot;direct&quot;</span><span class="p">,</span>
    <span class="n">dns</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;CNAME&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;ssh.example.com&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">origin_directs</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;tcp://109.151.40.129:22&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>argo_smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – . Enables Argo Smart Routing. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The name and type of DNS record for the Spectrum application. Fields documented below.</p></li>
<li><p><strong>edge_ip_connectivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>edge_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – . A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires <a class="reference external" href="https://developers.cloudflare.com/spectrum/getting-started/byoip/">Bring Your Own IP</a> provisioned.</p></li>
<li><p><strong>ip_firewall</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>origin_directs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p></li>
<li><p><strong>origin_dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A destination DNS addresses to the origin. Fields documented below.</p></li>
<li><p><strong>origin_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p></li>
<li><p><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>traffic_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the application to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of DNS record associated with the application. Valid values: <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>.</p></li>
</ul>
<p>The <strong>origin_dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.argo_smart_routing">
<code class="sig-name descname">argo_smart_routing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.argo_smart_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>. Enables Argo Smart Routing. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.dns">
<code class="sig-name descname">dns</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The name and type of DNS record for the Spectrum application. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of DNS record associated with the application. Valid values: <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.edge_ip_connectivity">
<code class="sig-name descname">edge_ip_connectivity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.edge_ip_connectivity" title="Permalink to this definition">¶</a></dt>
<dd><p>. Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.edge_ips">
<code class="sig-name descname">edge_ips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.edge_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>. A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires <a class="reference external" href="https://developers.cloudflare.com/spectrum/getting-started/byoip/">Bring Your Own IP</a> provisioned.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.ip_firewall">
<code class="sig-name descname">ip_firewall</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.ip_firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_directs">
<code class="sig-name descname">origin_directs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_directs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_dns">
<code class="sig-name descname">origin_dns</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>A destination DNS addresses to the origin. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_port">
<code class="sig-name descname">origin_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_port" title="Permalink to this definition">¶</a></dt>
<dd><p>If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.proxy_protocol">
<code class="sig-name descname">proxy_protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.proxy_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.tls">
<code class="sig-name descname">tls</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.tls" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.traffic_type">
<code class="sig-name descname">traffic_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.traffic_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to add the application to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">argo_smart_routing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_ip_connectivity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_firewall</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_directs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">traffic_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SpectrumApplication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>argo_smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – . Enables Argo Smart Routing. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The name and type of DNS record for the Spectrum application. Fields documented below.</p></li>
<li><p><strong>edge_ip_connectivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>edge_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>. A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires <a class="reference external" href="https://developers.cloudflare.com/spectrum/getting-started/byoip/">Bring Your Own IP</a> provisioned.</p>
</p></li>
<li><p><strong>ip_firewall</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>origin_directs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p></li>
<li><p><strong>origin_dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A destination DNS addresses to the origin. Fields documented below.</p></li>
<li><p><strong>origin_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p></li>
<li><p><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>traffic_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the application to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of DNS record associated with the application. Valid values: <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>.</p></li>
</ul>
<p>The <strong>origin_dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.SpectrumApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.SpectrumApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule group resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall groups.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">honey_pot</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WafGroup</span><span class="p">(</span><span class="s2">&quot;honeyPot&quot;</span><span class="p">,</span>
    <span class="n">group_id</span><span class="o">=</span><span class="s2">&quot;de677e5818985db1285d0e80225f06e5&quot;</span><span class="p">,</span>
    <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;on&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;ae36f999674d196762efcc5abb06b345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule Group ID.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the group, can be one of [“on”, “off”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.WafGroup.group_id">
<code class="sig-name descname">group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafGroup.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Rule Group ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafGroup.mode">
<code class="sig-name descname">mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafGroup.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of the group, can be one of [“on”, “off”].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafGroup.package_id">
<code class="sig-name descname">package_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafGroup.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafGroup.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafGroup.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule Group ID.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the group, can be one of [“on”, “off”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafPackage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafPackage</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sensitivity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule package resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall packages.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">owasp</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WafPackage</span><span class="p">(</span><span class="s2">&quot;owasp&quot;</span><span class="p">,</span>
    <span class="n">action_mode</span><span class="o">=</span><span class="s2">&quot;simulate&quot;</span><span class="p">,</span>
    <span class="n">package_id</span><span class="o">=</span><span class="s2">&quot;a25a9a7e9c00afc1fb2e0245519d725b&quot;</span><span class="p">,</span>
    <span class="n">sensitivity</span><span class="o">=</span><span class="s2">&quot;medium&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;ae36f999674d196762efcc5abb06b345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Package ID.</p></li>
<li><p><strong>sensitivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.WafPackage.action_mode">
<code class="sig-name descname">action_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafPackage.action_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafPackage.package_id">
<code class="sig-name descname">package_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafPackage.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Package ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafPackage.sensitivity">
<code class="sig-name descname">sensitivity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafPackage.sensitivity" title="Permalink to this definition">¶</a></dt>
<dd><p>The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafPackage.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafPackage.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafPackage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sensitivity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafPackage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Package ID.</p></li>
<li><p><strong>sensitivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafPackage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafPackage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall rules.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">_100000</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WafRule</span><span class="p">(</span><span class="s2">&quot;100000&quot;</span><span class="p">,</span>
    <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;simulate&quot;</span><span class="p">,</span>
    <span class="n">rule_id</span><span class="o">=</span><span class="s2">&quot;100000&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;ae36f999674d196762efcc5abb06b345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the rule.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule ID.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.WafRule.group_id">
<code class="sig-name descname">group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Group that contains the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafRule.mode">
<code class="sig-name descname">mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafRule.package_id">
<code class="sig-name descname">package_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafRule.rule_id">
<code class="sig-name descname">rule_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Rule ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WafRule.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Group that contains the rule.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the rule.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule ID.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WafRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerRoute">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkerRoute</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare worker route resource. A route will also require a <code class="docutils literal notranslate"><span class="pre">.WorkerScript</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">my_script</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkerScript</span><span class="p">(</span><span class="s2">&quot;myScript&quot;</span><span class="p">)</span>
<span class="c1"># see &quot;.WorkerScript&quot; documentation ...</span>
<span class="c1"># Runs the specified worker script for all URLs that match `example.com/*`</span>
<span class="n">my_route</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkerRoute</span><span class="p">(</span><span class="s2">&quot;myRoute&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">,</span>
    <span class="n">pattern</span><span class="o">=</span><span class="s2">&quot;example.com/*&quot;</span><span class="p">,</span>
    <span class="n">script_name</span><span class="o">=</span><span class="n">my_script</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p></li>
<li><p><strong>script_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which worker script to run for requests that match the route pattern. If <code class="docutils literal notranslate"><span class="pre">script_name</span></code> is empty, workers will be skipped for matching requests.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the route to.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkerRoute.pattern">
<code class="sig-name descname">pattern</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkerRoute.script_name">
<code class="sig-name descname">script_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.script_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Which worker script to run for requests that match the route pattern. If <code class="docutils literal notranslate"><span class="pre">script_name</span></code> is empty, workers will be skipped for matching requests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkerRoute.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to add the route to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerRoute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkerRoute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p>
</p></li>
<li><p><strong>script_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which worker script to run for requests that match the route pattern. If <code class="docutils literal notranslate"><span class="pre">script_name</span></code> is empty, workers will be skipped for matching requests.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the route to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerRoute.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerRoute.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerScript">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkerScript</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kv_namespace_bindings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare worker script resource. In order for a script to be active, you’ll also need to setup a <code class="docutils literal notranslate"><span class="pre">.WorkerRoute</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">my_namespace</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkersKvNamespace</span><span class="p">(</span><span class="s2">&quot;myNamespace&quot;</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
<span class="c1"># Sets the script with the name &quot;script_1&quot;</span>
<span class="n">my_script</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkerScript</span><span class="p">(</span><span class="s2">&quot;myScript&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;script_1&quot;</span><span class="p">,</span>
    <span class="n">content</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;script.js&quot;</span><span class="p">),</span>
    <span class="n">kv_namespace_binding</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;my_binding&quot;</span><span class="p">,</span>
        <span class="s2">&quot;namespaceId&quot;</span><span class="p">:</span> <span class="n">my_namespace</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script content.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the binding.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>kv_namespace_bindings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for the binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of KV namespace.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkerScript.content">
<code class="sig-name descname">content</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The script content.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkerScript.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the binding.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerScript.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kv_namespace_bindings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkerScript resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script content.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the binding.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>kv_namespace_bindings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for the binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of KV namespace.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkerScript.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerScript.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKv">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkersKv</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Workers KV Pair.  <em>NOTE:</em>  This resource uses the Cloudflare account APIs.  This requires setting the <code class="docutils literal notranslate"><span class="pre">CLOUDFLARE_ACCOUNT_ID</span></code> environment variable or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> provider argument.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example_ns</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkersKvNamespace</span><span class="p">(</span><span class="s2">&quot;exampleNs&quot;</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s2">&quot;test-namespace&quot;</span><span class="p">)</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkersKv</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">namespace_id</span><span class="o">=</span><span class="n">example_ns</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;test-key&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;test value&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Workers KV namespace in which you want to create the KV pair</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string value to be stored in the key</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkersKv.key">
<code class="sig-name descname">key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkersKv.namespace_id">
<code class="sig-name descname">namespace_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Workers KV namespace in which you want to create the KV pair</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkersKv.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The string value to be stored in the key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKv.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkersKv resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Workers KV namespace in which you want to create the KV pair</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string value to be stored in the key</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKv.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKv.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKvNamespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkersKvNamespace</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Workers KV Namespace</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">WorkersKvNamespace</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s2">&quot;test-namespace&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace you wish to create.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.WorkersKvNamespace.title">
<code class="sig-name descname">title</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the namespace you wish to create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKvNamespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkersKvNamespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace you wish to create.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.WorkersKvNamespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKvNamespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jump_start</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone resource. Zone is the basic resource for working with Cloudflare and is roughly equivalent to a domain name that the user purchases.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">Zone</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">zone</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>jump_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone name which will be added.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.jump_start">
<code class="sig-name descname">jump_start</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.jump_start" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.name_servers">
<code class="sig-name descname">name_servers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloudflare-assigned name servers. This is only populated for zones that use Cloudflare DNS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.paused">
<code class="sig-name descname">paused</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.plan">
<code class="sig-name descname">plan</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the zone. Valid values: <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">initializing</span></code>, <code class="docutils literal notranslate"><span class="pre">moved</span></code>, <code class="docutils literal notranslate"><span class="pre">deleted</span></code>, <code class="docutils literal notranslate"><span class="pre">deactivated</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.type" title="Permalink to this definition">¶</a></dt>
<dd><p>A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.vanity_name_servers">
<code class="sig-name descname">vanity_name_servers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.vanity_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Vanity Nameservers (if set).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">meta.wildcard_proxiable</span></code> - Indicates whether wildcard DNS records can receive Cloudflare security and performance features.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">meta.phishing_detected</span></code> - Indicates if URLs on the zone have been identified as hosting phishing content.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.verification_key">
<code class="sig-name descname">verification_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.verification_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the TXT record value to validate domain ownership. This is only populated for zones of type <code class="docutils literal notranslate"><span class="pre">partial</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.Zone.zone">
<code class="sig-name descname">zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone name which will be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jump_start</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vanity_name_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>jump_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p></li>
<li><p><strong>name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cloudflare-assigned name servers. This is only populated for zones that use Cloudflare DNS.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the zone. Valid values: <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">initializing</span></code>, <code class="docutils literal notranslate"><span class="pre">moved</span></code>, <code class="docutils literal notranslate"><span class="pre">deleted</span></code>, <code class="docutils literal notranslate"><span class="pre">deactivated</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p></li>
<li><p><strong>vanity_name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Vanity Nameservers (if set).</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `meta.wildcard_proxiable` - Indicates whether wildcard DNS records can receive Cloudflare security and performance features.
* `meta.phishing_detected` - Indicates if URLs on the zone have been identified as hosting phishing content.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>verification_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the TXT record value to validate domain ownership. This is only populated for zones of type <code class="docutils literal notranslate"><span class="pre">partial</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone name which will be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>meta</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">phishing_detected</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wildcard_proxiable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneLockdown">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ZoneLockdown</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone Lockdown resource. Zone Lockdown allows you to define one or more URLs (with wildcard matching on the domain or path) that will only permit access if the request originates from an IP address that matches a safelist of one or more IP addresses and/or IP ranges.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="c1"># Restrict access to these endpoints to requests from a known IP address.</span>
<span class="n">endpoint_lockdown</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneLockdown</span><span class="p">(</span><span class="s2">&quot;endpointLockdown&quot;</span><span class="p">,</span>
    <span class="n">configurations</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;ip&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;198.51.100.4&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Restrict access to these endpoints to requests from a known IP address&quot;</span><span class="p">,</span>
    <span class="n">paused</span><span class="o">=</span><span class="s2">&quot;false&quot;</span><span class="p">,</span>
    <span class="n">urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;api.mysite.com/some/endpoint*&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone lockdown is currently paused. Default: false.</p></li>
<li><p><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request property to target. Allowed values: “ip”, “ip_range”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to target. Depends on target’s type. IP addresses should just be standard IPv4/IPv6 notation i.e. <code class="docutils literal notranslate"><span class="pre">198.51.100.4</span></code> or <code class="docutils literal notranslate"><span class="pre">2001:db8::/32</span></code> and IP ranges in CIDR format i.e. <code class="docutils literal notranslate"><span class="pre">198.51.0.0/16</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.configurations">
<code class="sig-name descname">configurations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The request property to target. Allowed values: “ip”, “ip_range”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to target. Depends on target’s type. IP addresses should just be standard IPv4/IPv6 notation i.e. <code class="docutils literal notranslate"><span class="pre">198.51.100.4</span></code> or <code class="docutils literal notranslate"><span class="pre">2001:db8::/32</span></code> and IP ranges in CIDR format i.e. <code class="docutils literal notranslate"><span class="pre">198.51.0.0/16</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.paused">
<code class="sig-name descname">paused</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether this zone lockdown is currently paused. Default: false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.urls">
<code class="sig-name descname">urls</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which the access rule should be added.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneLockdown resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone lockdown is currently paused. Default: false.</p></li>
<li><p><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request property to target. Allowed values: “ip”, “ip_range”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to target. Depends on target’s type. IP addresses should just be standard IPv4/IPv6 notation i.e. <code class="docutils literal notranslate"><span class="pre">198.51.100.4</span></code> or <code class="docutils literal notranslate"><span class="pre">2001:db8::/32</span></code> and IP ranges in CIDR format i.e. <code class="docutils literal notranslate"><span class="pre">198.51.0.0/16</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneLockdown.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneLockdown.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneSettingsOverride">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ZoneSettingsOverride</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which customizes Cloudflare zone settings. Note that after destroying this resource Zone Settings will be reset to their initial values.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneSettingsOverride</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cloudflare_zone_id&quot;</span><span class="p">],</span>
    <span class="n">settings</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;brotli&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="s2">&quot;challengeTtl&quot;</span><span class="p">:</span> <span class="mi">2700</span><span class="p">,</span>
        <span class="s2">&quot;securityLevel&quot;</span><span class="p">:</span> <span class="s2">&quot;high&quot;</span><span class="p">,</span>
        <span class="s2">&quot;opportunisticEncryption&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="s2">&quot;automaticHttpsRewrites&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="s2">&quot;mirage&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="s2">&quot;waf&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="s2">&quot;minify&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;css&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
            <span class="s2">&quot;js&quot;</span><span class="p">:</span> <span class="s2">&quot;off&quot;</span><span class="p">,</span>
            <span class="s2">&quot;html&quot;</span><span class="p">:</span> <span class="s2">&quot;off&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;security_header&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which apply settings.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universalSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - . Note that the value specified will be ignored unless <code class="docutils literal notranslate"><span class="pre">polish</span></code> is turned on (i.e. is “lossless” or “lossy”)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.initial_settings">
<code class="sig-name descname">initial_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.initial_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings present in the zone at the time the resource is created. This will be used to restore the original settings when this resource is destroyed. Shares the same schema as the <code class="docutils literal notranslate"><span class="pre">settings</span></code> attribute (Above).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universalSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - . Note that the value specified will be ignored unless <code class="docutils literal notranslate"><span class="pre">polish</span></code> is turned on (i.e. is “lossless” or “lossy”)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.readonly_settings">
<code class="sig-name descname">readonly_settings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.readonly_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Which of the current <code class="docutils literal notranslate"><span class="pre">settings</span></code> are not able to be set by the user. Which settings these are is determined by plan level and user permissions.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">zone_status</span></code>. A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone_type</span></code>. Status of the zone. Valid values: active, pending, initializing, moved, deleted, deactivated.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.settings">
<code class="sig-name descname">settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universalSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - . Note that the value specified will be ignored unless <code class="docutils literal notranslate"><span class="pre">polish</span></code> is turned on (i.e. is “lossless” or “lossy”)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which apply settings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_settings_read_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">readonly_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneSettingsOverride resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>initial_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings present in the zone at the time the resource is created. This will be used to restore the original settings when this resource is destroyed. Shares the same schema as the <code class="docutils literal notranslate"><span class="pre">settings</span></code> attribute (Above).</p></li>
<li><p><strong>readonly_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Which of the current <code class="docutils literal notranslate"><span class="pre">settings</span></code> are not able to be set by the user. Which settings these are is determined by plan level and user permissions.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `zone_status`. A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup.
* `zone_type`. Status of the zone. Valid values: active, pending, initializing, moved, deleted, deactivated.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which apply settings.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>initial_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universalSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - . Note that the value specified will be ignored unless <code class="docutils literal notranslate"><span class="pre">polish</span></code> is turned on (i.e. is “lossless” or “lossy”)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">universalSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - . Note that the value specified will be ignored unless <code class="docutils literal notranslate"><span class="pre">polish</span></code> is turned on (i.e. is “lossless” or “lossy”)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneSettingsOverride.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.get_ip_ranges">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the <a class="reference external" href="https://www.cloudflare.com/ips/">IP ranges</a> of Cloudflare edge nodes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">cloudflare</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_ip_ranges</span><span class="p">()</span>
<span class="n">allow_cloudflare_ingress</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">compute</span><span class="o">.</span><span class="n">Firewall</span><span class="p">(</span><span class="s2">&quot;allowCloudflareIngress&quot;</span><span class="p">,</span>
    <span class="n">network</span><span class="o">=</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">source_ranges</span><span class="o">=</span><span class="n">cloudflare</span><span class="o">.</span><span class="n">ipv4_cidr_blocks</span><span class="p">,</span>
    <span class="n">allow</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;ports&quot;</span><span class="p">:</span> <span class="s2">&quot;443&quot;</span><span class="p">,</span>
        <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_waf_groups">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_waf_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://api.cloudflare.com/#waf-rule-groups-properties">WAF Rule Groups</a>.</p>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_waf_packages">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_packages</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_waf_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://api.cloudflare.com/#waf-rule-packages-properties">WAF Rule Packages</a>.</p>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action_mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">detectionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sensitivity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_waf_rules">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_waf_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://api.cloudflare.com/#waf-rule-groups-properties">WAF Rules</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_waf_rules</span><span class="p">(</span><span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;ae36f999674d196762efcc5abb06b345&quot;</span><span class="p">,</span>
    <span class="n">package_id</span><span class="o">=</span><span class="s2">&quot;a25a9a7e9c00afc1fb2e0245519d725b&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;.*example.*&quot;</span><span class="p">,</span>
        <span class="s2">&quot;mode&quot;</span><span class="p">:</span> <span class="s2">&quot;on&quot;</span><span class="p">,</span>
        <span class="s2">&quot;groupId&quot;</span><span class="p">:</span> <span class="s2">&quot;de677e5818985db1285d0e80225f06e5&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;wafRules&quot;</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">rules</span><span class="p">)</span>
</pre></div>
</div>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudflare.get_zones">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up <a class="reference external" href="https://api.cloudflare.com/#zone-properties">Zone</a> records.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudflare</span> <span class="k">as</span> <span class="nn">cloudflare</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="nb">filter</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;example.*&quot;</span><span class="p">,</span>
    <span class="s2">&quot;paused&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
    <span class="s2">&quot;status&quot;</span><span class="p">:</span> <span class="s2">&quot;active&quot;</span><span class="p">,</span>
<span class="p">})</span>
<span class="n">endpoint_lockdown</span> <span class="o">=</span> <span class="n">cloudflare</span><span class="o">.</span><span class="n">ZoneLockdown</span><span class="p">(</span><span class="s2">&quot;endpointLockdown&quot;</span><span class="p">,</span>
    <span class="n">configurations</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;ip&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;198.51.100.4&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Restrict access to these endpoints to requests from a known IP address&quot;</span><span class="p">,</span>
    <span class="n">paused</span><span class="o">=</span><span class="s2">&quot;false&quot;</span><span class="p">,</span>
    <span class="n">urls</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;api.mysite.com/some/endpoint*&quot;</span><span class="p">],</span>
    <span class="n">zone</span><span class="o">=</span><span class="n">test</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paused</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

</div>
