---
title: Package pulumi_consul
title_tag: Package pulumi_consul | Python SDK
linktitle: pulumi_consul
notitle: true
---

<div class="section" id="pulumi-consul">
<h1>Pulumi Consul<a class="headerlink" href="#pulumi-consul" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-consul">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-consul/issues">pulumi/pulumi-consul repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-consul/issues">terraform-providers/terraform-provider-consul repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_consul"></span><dl class="py class">
<dt id="pulumi_consul.AclAuthMethod">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AclAuthMethod</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclAuthMethod" title="Permalink to this definition">¶</a></dt>
<dd><p>Starting with Consul 1.5.0, the .AclAuthMethod resource can be used to
managed Consul ACL auth methods.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The raw configuration for this ACL auth method.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A free form human readable description of the auth method.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ACL auth method.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the policy within.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the ACL auth method.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.AclAuthMethod.config">
<code class="sig-name descname">config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclAuthMethod.config" title="Permalink to this definition">¶</a></dt>
<dd><p>The raw configuration for this ACL auth method.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclAuthMethod.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclAuthMethod.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A free form human readable description of the auth method.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclAuthMethod.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclAuthMethod.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ACL auth method.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclAuthMethod.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclAuthMethod.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace to create the policy within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclAuthMethod.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclAuthMethod.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the ACL auth method.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclAuthMethod.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclAuthMethod.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AclAuthMethod resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The raw configuration for this ACL auth method.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A free form human readable description of the auth method.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ACL auth method.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the policy within.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the ACL auth method.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclAuthMethod.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclAuthMethod.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclAuthMethod.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclAuthMethod.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclBindingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AclBindingRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bind_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bind_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclBindingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Starting with Consul 1.5.0, the .AclBindingRule resource can be used to
managed Consul ACL binding rules.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ACL auth method this rule apply.</p></li>
<li><p><strong>bind_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to bind to a token at login-time.</p></li>
<li><p><strong>bind_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the way the binding rule affects a token
created at login.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A free form human readable description of the
binding rule.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the binding
rule within.</p></li>
<li><p><strong>selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expression used to math this rule against valid
identities returned from an auth method validation.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.AclBindingRule.auth_method">
<code class="sig-name descname">auth_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclBindingRule.auth_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ACL auth method this rule apply.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclBindingRule.bind_name">
<code class="sig-name descname">bind_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclBindingRule.bind_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to bind to a token at login-time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclBindingRule.bind_type">
<code class="sig-name descname">bind_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclBindingRule.bind_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the way the binding rule affects a token
created at login.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclBindingRule.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclBindingRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A free form human readable description of the
binding rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclBindingRule.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclBindingRule.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace to create the binding
rule within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclBindingRule.selector">
<code class="sig-name descname">selector</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclBindingRule.selector" title="Permalink to this definition">¶</a></dt>
<dd><p>The expression used to math this rule against valid
identities returned from an auth method validation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclBindingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bind_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bind_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclBindingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AclBindingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ACL auth method this rule apply.</p></li>
<li><p><strong>bind_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to bind to a token at login-time.</p></li>
<li><p><strong>bind_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the way the binding rule affects a token
created at login.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A free form human readable description of the
binding rule.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the binding
rule within.</p></li>
<li><p><strong>selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expression used to math this rule against valid
identities returned from an auth method validation.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclBindingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclBindingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclBindingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclBindingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AclPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Starting with Consul 1.4.0, the .AclPolicy can be used to managed Consul ACL policies.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>datacenters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The datacenters of the policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the policy within.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rules of the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.AclPolicy.datacenters">
<code class="sig-name descname">datacenters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclPolicy.datacenters" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenters of the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclPolicy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclPolicy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclPolicy.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclPolicy.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace to create the policy within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclPolicy.rules">
<code class="sig-name descname">rules</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclPolicy.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The rules of the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AclPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>datacenters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The datacenters of the policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the policy within.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rules of the policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AclRole</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Starting with Consul 1.5.0, the .AclRole can be used to managed Consul ACL roles.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A free form human readable description of the role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ACL role.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the role within.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of policies that should be applied to the role.</p></li>
<li><p><strong>service_identities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of service identities that should
be applied to the role.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>service_identities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The datacenters the effective policy is valid within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the service.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_consul.AclRole.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclRole.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A free form human readable description of the role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclRole.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ACL role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclRole.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclRole.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace to create the role within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclRole.policies">
<code class="sig-name descname">policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of policies that should be applied to the role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclRole.service_identities">
<code class="sig-name descname">service_identities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclRole.service_identities" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of service identities that should
be applied to the role.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The datacenters the effective policy is valid within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the service.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_identities</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AclRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A free form human readable description of the role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ACL role.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the role within.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of policies that should be applied to the role.</p></li>
<li><p><strong>service_identities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of service identities that should
be applied to the role.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>service_identities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The datacenters the effective policy is valid within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the service.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AclToken</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclToken" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.AclToken</span></code> resource writes an ACL token into Consul.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The uuid of the token. If omitted, Consul will
generate a random uuid.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the token.</p></li>
<li><p><strong>local</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The flag to set the token local to the current datacenter.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the token within.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of policies attached to the token.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of roles attached to the token.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.AclToken.accessor_id">
<code class="sig-name descname">accessor_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclToken.accessor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The uuid of the token. If omitted, Consul will
generate a random uuid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclToken.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclToken.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclToken.local">
<code class="sig-name descname">local</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclToken.local" title="Permalink to this definition">¶</a></dt>
<dd><p>The flag to set the token local to the current datacenter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclToken.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclToken.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace to create the token within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclToken.policies">
<code class="sig-name descname">policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclToken.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of policies attached to the token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclToken.roles">
<code class="sig-name descname">roles</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclToken.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of roles attached to the token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclToken.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AclToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The uuid of the token. If omitted, Consul will
generate a random uuid.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the token.</p></li>
<li><p><strong>local</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The flag to set the token local to the current datacenter.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the token within.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of policies attached to the token.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of roles attached to the token.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclToken.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclToken.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclTokenPolicyAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AclTokenPolicyAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclTokenPolicyAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AclTokenPolicyAttachment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] policy: The name of the policy attached to the token.
:param pulumi.Input[str] token_id: The id of the token.</p>
<dl class="py attribute">
<dt id="pulumi_consul.AclTokenPolicyAttachment.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclTokenPolicyAttachment.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy attached to the token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AclTokenPolicyAttachment.token_id">
<code class="sig-name descname">token_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AclTokenPolicyAttachment.token_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclTokenPolicyAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclTokenPolicyAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AclTokenPolicyAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy attached to the token.</p></li>
<li><p><strong>token_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the token.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AclTokenPolicyAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclTokenPolicyAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AclTokenPolicyAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AclTokenPolicyAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AgentService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AgentService</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AgentService" title="Permalink to this definition">¶</a></dt>
<dd><p>!&gt; The <code class="docutils literal notranslate"><span class="pre">.AgentService</span></code> resource has been deprecated in version 2.0.0 of the provider
and will be removed in a future release. Please read the <a class="reference external" href="https://www.terraform.io/docs/providers/consul/guides/upgrading.html#deprecation-of-consul_agent_service">upgrade guide</a>
for more information.</p>
<p>Provides access to the agent service data in Consul. This can be used to
define a service associated with a particular agent. Currently, defining
health checks for an agent service is not supported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the service. Defaults to the
address of the agent.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port of the service.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.AgentService.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AgentService.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The address of the service. Defaults to the
address of the agent.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AgentService.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AgentService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AgentService.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AgentService.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port of the service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AgentService.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AgentService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AgentService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AgentService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AgentService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the service. Defaults to the
address of the agent.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port of the service.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AgentService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AgentService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AgentService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AgentService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AutopilotConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AutopilotConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cleanup_dead_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_upgrade_migration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_contact_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_trailing_logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redundancy_zone_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_stabilization_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">upgrade_version_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AutopilotConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to the <a class="reference external" href="https://www.consul.io/docs/guides/autopilot.html">Autopilot Configuration</a>
of Consul to automatically manage Consul servers.</p>
<p>It includes to automatically cleanup dead servers, monitor the status of the Raft
cluster and stable server introduction.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cleanup_dead_servers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to remove failing servers when a
replacement comes online. Defaults to true.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the agent’s
default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>disable_upgrade_migration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to disable <a class="reference external" href="https://www.consul.io/docs/guides/autopilot.html#redundancy-zones">upgrade migrations</a>.
Defaults to false.</p></li>
<li><p><strong>last_contact_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time after which a server is
considered as unhealthy and will be removed. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;200ms&quot;</span></code>.</p></li>
<li><p><strong>max_trailing_logs</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of Raft log entries a
server can trail the leader. Defaults to 250.</p></li>
<li><p><strong>redundancy_zone_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://www.consul.io/docs/guides/autopilot.html#redundancy-zones">redundancy zone</a>
tag to use. Consul will try to keep one voting server by zone to take advantage
of isolated failure domains. Defaults to an empty string.</p></li>
<li><p><strong>server_stabilization_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period to wait for a server to be
healthy and stable before being promoted to a full, voting member. Defaults to
<code class="docutils literal notranslate"><span class="pre">&quot;10s&quot;</span></code>.</p></li>
<li><p><strong>upgrade_version_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag to override the version information
used during a migration. Defaults to an empty string.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.AutopilotConfig.cleanup_dead_servers">
<code class="sig-name descname">cleanup_dead_servers</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AutopilotConfig.cleanup_dead_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to remove failing servers when a
replacement comes online. Defaults to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AutopilotConfig.datacenter">
<code class="sig-name descname">datacenter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AutopilotConfig.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter to use. This overrides the agent’s
default datacenter and the datacenter in the provider setup.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AutopilotConfig.disable_upgrade_migration">
<code class="sig-name descname">disable_upgrade_migration</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AutopilotConfig.disable_upgrade_migration" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to disable <a class="reference external" href="https://www.consul.io/docs/guides/autopilot.html#redundancy-zones">upgrade migrations</a>.
Defaults to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AutopilotConfig.last_contact_threshold">
<code class="sig-name descname">last_contact_threshold</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AutopilotConfig.last_contact_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The time after which a server is
considered as unhealthy and will be removed. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;200ms&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AutopilotConfig.max_trailing_logs">
<code class="sig-name descname">max_trailing_logs</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AutopilotConfig.max_trailing_logs" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of Raft log entries a
server can trail the leader. Defaults to 250.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AutopilotConfig.redundancy_zone_tag">
<code class="sig-name descname">redundancy_zone_tag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AutopilotConfig.redundancy_zone_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://www.consul.io/docs/guides/autopilot.html#redundancy-zones">redundancy zone</a>
tag to use. Consul will try to keep one voting server by zone to take advantage
of isolated failure domains. Defaults to an empty string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AutopilotConfig.server_stabilization_time">
<code class="sig-name descname">server_stabilization_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AutopilotConfig.server_stabilization_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The period to wait for a server to be
healthy and stable before being promoted to a full, voting member. Defaults to
<code class="docutils literal notranslate"><span class="pre">&quot;10s&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.AutopilotConfig.upgrade_version_tag">
<code class="sig-name descname">upgrade_version_tag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.AutopilotConfig.upgrade_version_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag to override the version information
used during a migration. Defaults to an empty string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AutopilotConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cleanup_dead_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_upgrade_migration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_contact_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_trailing_logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redundancy_zone_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_stabilization_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">upgrade_version_tag</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AutopilotConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AutopilotConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cleanup_dead_servers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to remove failing servers when a
replacement comes online. Defaults to true.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the agent’s
default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>disable_upgrade_migration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Whether to disable <a class="reference external" href="https://www.consul.io/docs/guides/autopilot.html#redundancy-zones">upgrade migrations</a>.
Defaults to false.</p>
</p></li>
<li><p><strong>last_contact_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time after which a server is
considered as unhealthy and will be removed. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;200ms&quot;</span></code>.</p></li>
<li><p><strong>max_trailing_logs</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of Raft log entries a
server can trail the leader. Defaults to 250.</p></li>
<li><p><strong>redundancy_zone_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://www.consul.io/docs/guides/autopilot.html#redundancy-zones">redundancy zone</a>
tag to use. Consul will try to keep one voting server by zone to take advantage
of isolated failure domains. Defaults to an empty string.</p>
</p></li>
<li><p><strong>server_stabilization_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period to wait for a server to be
healthy and stable before being promoted to a full, voting member. Defaults to
<code class="docutils literal notranslate"><span class="pre">&quot;10s&quot;</span></code>.</p></li>
<li><p><strong>upgrade_version_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag to override the version information
used during a migration. Defaults to an empty string.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.AutopilotConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AutopilotConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AutopilotConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AutopilotConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.AwaitableGetAclAuthMethodResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetAclAuthMethodResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetAclAuthMethodResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetAclPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetAclPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetAclPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetAclRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetAclRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_identities</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetAclRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetAclTokenResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetAclTokenResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accessor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetAclTokenResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetAclTokenSecretIdResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetAclTokenSecretIdResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accessor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_secret_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetAclTokenSecretIdResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetAgentConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetAgentConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetAgentConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetAgentSelfResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetAgentSelfResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acl_datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_disabled_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_down_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_enforce08_semantics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advertise_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advertise_addr_wan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advertise_addrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_join</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bind_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_expect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_deregister_interval_min</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_reap_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_update_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_dir</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dev_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_recursors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_anonymous_signature</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_coordinates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_debug</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_remote_exec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_syslog</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ui</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_update_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">leave_on_int</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">leave_on_term</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pid_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reconnect_timeout_lan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reconnect_timeout_wan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rejoin_after_leave</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_join_ec2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_join_gce</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_join_wans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_joins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_max_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_max_attempts_wan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serf_lan_bind_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serf_wan_bind_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_ttl_min</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_join_wans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_joins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syslog_facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tagged_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">telemetry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_ca_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_cert_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_min_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_verify_incoming</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_verify_outgoing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_verify_server_hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">translate_wan_addrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ui_dir</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unix_sockets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_prerelease</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_revision</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetAgentSelfResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetAutopilotHealthResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetAutopilotHealthResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">failure_tolerance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetAutopilotHealthResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetCatalogNodesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetCatalogNodesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetCatalogNodesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetCatalogServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetCatalogServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetCatalogServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetCatalogServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetCatalogServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetCatalogServicesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetKeyPrefixResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetKeyPrefixResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkey_collection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetKeyPrefixResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetKeysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetNodesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetNodesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetNodesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetServiceHealthResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetServiceHealthResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">near</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetServiceHealthResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.AwaitableGetServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">AwaitableGetServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.AwaitableGetServicesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_consul.CatalogEntry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">CatalogEntry</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.CatalogEntry" title="Permalink to this definition">¶</a></dt>
<dd><p>!&gt; The <code class="docutils literal notranslate"><span class="pre">.CatalogEntry</span></code> resource has been deprecated in version 2.0.0 of the provider
and will be removed in a future release. Please read the <a class="reference external" href="https://www.terraform.io/docs/providers/consul/guides/upgrading.html#deprecation-of-consul_catalog_entry">upgrade guide</a>
for more information.</p>
<p>Registers a node or service with the <a class="reference external" href="https://www.consul.io/docs/agent/http/catalog.html#catalog_register">Consul Catalog</a>.
Currently, defining health checks is not supported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the node being added to,
or referenced in the catalog.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>node</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node being added to, or
referenced in the catalog.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A service to optionally associated with
the node. Supported values are documented below.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ACL token.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address of the service. Defaults to the
node address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the service. Defaults to the <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the service</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port of the service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_consul.CatalogEntry.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.CatalogEntry.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The address of the node being added to,
or referenced in the catalog.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.CatalogEntry.datacenter">
<code class="sig-name descname">datacenter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.CatalogEntry.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.CatalogEntry.node">
<code class="sig-name descname">node</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.CatalogEntry.node" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the node being added to, or
referenced in the catalog.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.CatalogEntry.services">
<code class="sig-name descname">services</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.CatalogEntry.services" title="Permalink to this definition">¶</a></dt>
<dd><p>A service to optionally associated with
the node. Supported values are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The address of the service. Defaults to the
node address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the service. Defaults to the <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the service</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port of the service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.CatalogEntry.token">
<code class="sig-name descname">token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.CatalogEntry.token" title="Permalink to this definition">¶</a></dt>
<dd><p>ACL token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.CatalogEntry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.CatalogEntry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CatalogEntry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the node being added to,
or referenced in the catalog.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>node</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node being added to, or
referenced in the catalog.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A service to optionally associated with
the node. Supported values are documented below.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ACL token.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address of the service. Defaults to the
node address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the service. Defaults to the <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the service</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port of the service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.CatalogEntry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.CatalogEntry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.CatalogEntry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.CatalogEntry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.ConfigEntry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">ConfigEntry</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.ConfigEntry" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://www.consul.io/docs/agent/config_entries.html">Configuration Entry</a>
resource can be used to provide cluster-wide defaults for various aspects of
Consul.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An arbitrary map of configuration values.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of configuration entry to register.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration entry being registred.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.ConfigEntry.config_json">
<code class="sig-name descname">config_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.ConfigEntry.config_json" title="Permalink to this definition">¶</a></dt>
<dd><p>An arbitrary map of configuration values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.ConfigEntry.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.ConfigEntry.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of configuration entry to register.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.ConfigEntry.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.ConfigEntry.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration entry being registred.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.ConfigEntry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.ConfigEntry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConfigEntry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An arbitrary map of configuration values.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of configuration entry to register.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration entry being registred.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.ConfigEntry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.ConfigEntry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.ConfigEntry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.ConfigEntry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.GetAclAuthMethodResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetAclAuthMethodResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetAclAuthMethodResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAclAuthMethod.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetAclAuthMethodResult.config">
<code class="sig-name descname">config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclAuthMethodResult.config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration options of the ACL Auth Method.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclAuthMethodResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclAuthMethodResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the ACL Auth Method.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclAuthMethodResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclAuthMethodResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclAuthMethodResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclAuthMethodResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the ACL Auth Method.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetAclPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetAclPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetAclPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAclPolicy.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetAclPolicyResult.datacenters">
<code class="sig-name descname">datacenters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclPolicyResult.datacenters" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenters associated with the ACL Policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclPolicyResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclPolicyResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the ACL Policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclPolicyResult.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclPolicyResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The rules associated with the ACL Policy.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetAclRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetAclRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_identities</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetAclRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAclRole.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetAclRoleResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclRoleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the ACL Role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclRoleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclRoleResult.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclRoleResult.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of policies associated with the ACL Role. Each entry has
an <code class="docutils literal notranslate"><span class="pre">id</span></code> and a <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclRoleResult.service_identities">
<code class="sig-name descname">service_identities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclRoleResult.service_identities" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of service identities associated with the ACL
Role. Each entry has a <code class="docutils literal notranslate"><span class="pre">service_name</span></code> attribute and a list of <code class="docutils literal notranslate"><span class="pre">datacenters</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetAclTokenResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetAclTokenResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accessor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetAclTokenResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAclToken.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetAclTokenResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclTokenResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the ACL token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclTokenResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclTokenResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclTokenResult.local">
<code class="sig-name descname">local</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclTokenResult.local" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the ACL token is local to the datacenter it was created within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclTokenResult.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclTokenResult.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policies associated with the ACL token. Each entry has
an <code class="docutils literal notranslate"><span class="pre">id</span></code> and a <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetAclTokenSecretIdResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetAclTokenSecretIdResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accessor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_secret_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetAclTokenSecretIdResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAclTokenSecretId.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetAclTokenSecretIdResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclTokenSecretIdResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAclTokenSecretIdResult.secret_id">
<code class="sig-name descname">secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAclTokenSecretIdResult.secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret ID of the ACL token if <code class="docutils literal notranslate"><span class="pre">gpg_key</span></code> has not been set.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetAgentConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetAgentConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetAgentConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAgentConfig.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetAgentConfigResult.datacenter">
<code class="sig-name descname">datacenter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentConfigResult.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter the agent is running in</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAgentConfigResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAgentConfigResult.node_id">
<code class="sig-name descname">node_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentConfigResult.node_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the node the agent is running on</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAgentConfigResult.node_name">
<code class="sig-name descname">node_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentConfigResult.node_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the node the agent is running on</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAgentConfigResult.revision">
<code class="sig-name descname">revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentConfigResult.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The first 9 characters of the VCS revision of the build of Consul that is running</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAgentConfigResult.server">
<code class="sig-name descname">server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentConfigResult.server" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean if the agent is a server or not</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAgentConfigResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentConfigResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the build of Consul that is running</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetAgentSelfResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetAgentSelfResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acl_datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_disabled_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_down_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_enforce08_semantics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advertise_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advertise_addr_wan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advertise_addrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_join</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bind_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_expect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_deregister_interval_min</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_reap_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_update_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_dir</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dev_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_recursors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_anonymous_signature</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_coordinates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_debug</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_remote_exec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_syslog</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ui</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_update_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">leave_on_int</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">leave_on_term</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">performance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pid_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reconnect_timeout_lan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reconnect_timeout_wan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rejoin_after_leave</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_join_ec2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_join_gce</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_join_wans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_joins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_max_attempts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_max_attempts_wan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serf_lan_bind_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serf_wan_bind_addr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_ttl_min</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_join_wans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_joins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syslog_facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tagged_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">telemetry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_ca_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_cert_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_min_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_verify_incoming</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_verify_outgoing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_verify_server_hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">translate_wan_addrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ui_dir</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unix_sockets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_prerelease</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_revision</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetAgentSelfResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAgentSelf.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetAgentSelfResult.dns">
<code class="sig-name descname">dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentSelfResult.dns" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of DNS configuration attributes.  See below for details on the
contents of the <code class="docutils literal notranslate"><span class="pre">dns</span></code> attribute.</p>
<ul class="simple">
<li><p><cite>``dns_recursors`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#recursors">https://www.consul.io/docs/agent/options.html#recursors</a>&gt;`_ - A
list of all DNS recursors.</p></li>
<li><p><cite>``data_dir`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_data_dir">https://www.consul.io/docs/agent/options.html#_data_dir</a>&gt;`_</p></li>
<li><p><cite>``datacenter`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_datacenter">https://www.consul.io/docs/agent/options.html#_datacenter</a>&gt;`_</p></li>
<li><p><cite>``dev_mode`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_dev">https://www.consul.io/docs/agent/options.html#_dev</a>&gt;`_</p></li>
<li><p><cite>``domain`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_domain">https://www.consul.io/docs/agent/options.html#_domain</a>&gt;`_</p></li>
<li><p><cite>``enable_anonymous_signature`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#disable_anonymous_signature">https://www.consul.io/docs/agent/options.html#disable_anonymous_signature</a>&gt;`_</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_coordinates</span></code></p></li>
<li><p><cite>``enable_debug`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#enable_debug">https://www.consul.io/docs/agent/options.html#enable_debug</a>&gt;`_</p></li>
<li><p><cite>``enable_remote_exec`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#disable_remote_exec">https://www.consul.io/docs/agent/options.html#disable_remote_exec</a>&gt;`_</p></li>
<li><p><cite>``enable_syslog`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_syslog">https://www.consul.io/docs/agent/options.html#_syslog</a>&gt;`_</p></li>
<li><p><cite>``enable_ui`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_ui">https://www.consul.io/docs/agent/options.html#_ui</a>&gt;`_</p></li>
<li><p><cite>``enable_update_check`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#disable_update_check">https://www.consul.io/docs/agent/options.html#disable_update_check</a>&gt;`_</p></li>
<li><p><cite>``id`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_node_id">https://www.consul.io/docs/agent/options.html#_node_id</a>&gt;`_</p></li>
<li><p><cite>``leave_on_int`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#skip_leave_on_interrupt">https://www.consul.io/docs/agent/options.html#skip_leave_on_interrupt</a>&gt;`_</p></li>
<li><p><cite>``leave_on_term`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#leave_on_terminate">https://www.consul.io/docs/agent/options.html#leave_on_terminate</a>&gt;`_</p></li>
<li><p><cite>``log_level`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_log_level">https://www.consul.io/docs/agent/options.html#_log_level</a>&gt;`_</p></li>
<li><p><cite>``name`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_node">https://www.consul.io/docs/agent/options.html#_node</a>&gt;`_</p></li>
<li><p><cite>``performance`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#performance">https://www.consul.io/docs/agent/options.html#performance</a>&gt;`_</p></li>
<li><p><cite>``pid_file`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_pid_file">https://www.consul.io/docs/agent/options.html#_pid_file</a>&gt;`_</p></li>
<li><p><cite>``ports`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#ports">https://www.consul.io/docs/agent/options.html#ports</a>&gt;`_</p></li>
<li><p><cite>``protocol_version`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_protocol">https://www.consul.io/docs/agent/options.html#_protocol</a>&gt;`_</p></li>
<li><p><cite>``reconnect_timeout_lan`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#reconnect_timeout">https://www.consul.io/docs/agent/options.html#reconnect_timeout</a>&gt;`_</p></li>
<li><p><cite>``reconnect_timeout_wan`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#reconnect_timeout_wan">https://www.consul.io/docs/agent/options.html#reconnect_timeout_wan</a>&gt;`_</p></li>
<li><p><cite>``rejoin_after_leave`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_rejoin">https://www.consul.io/docs/agent/options.html#_rejoin</a>&gt;`_</p></li>
<li><p><cite>``retry_join`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#retry_join">https://www.consul.io/docs/agent/options.html#retry_join</a>&gt;`_</p></li>
<li><p><cite>``retry_join_ec2`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#retry_join_ec2">https://www.consul.io/docs/agent/options.html#retry_join_ec2</a>&gt;`_ -
A map of EC2 retry attributes.  See below for details on the available
information.</p></li>
<li><p><cite>``retry_join_gce`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#retry_join_gce">https://www.consul.io/docs/agent/options.html#retry_join_gce</a>&gt;`_ -
A map of GCE retry attributes.  See below for details on the available
information.</p></li>
<li><p><cite>``retry_join_wan`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_retry_join_wan">https://www.consul.io/docs/agent/options.html#_retry_join_wan</a>&gt;`_</p></li>
<li><p><cite>``retry_max_attempts`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_retry_max">https://www.consul.io/docs/agent/options.html#_retry_max</a>&gt;`_</p></li>
<li><p><cite>``retry_max_attempts_wan`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_retry_max_wan">https://www.consul.io/docs/agent/options.html#_retry_max_wan</a>&gt;`_</p></li>
<li><p><cite>``serf_lan_bind_addr`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_serf_lan_bind">https://www.consul.io/docs/agent/options.html#_serf_lan_bind</a>&gt;`_</p></li>
<li><p><cite>``serf_wan_bind_addr`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_serf_wan_bind">https://www.consul.io/docs/agent/options.html#_serf_wan_bind</a>&gt;`_</p></li>
<li><p><cite>``server_mode`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#_server">https://www.consul.io/docs/agent/options.html#_server</a>&gt;`_</p></li>
<li><p><cite>``server_name`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#server_name">https://www.consul.io/docs/agent/options.html#server_name</a>&gt;`_</p></li>
<li><p><cite>``session_ttl_min`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#session_ttl_min">https://www.consul.io/docs/agent/options.html#session_ttl_min</a>&gt;`_</p></li>
<li><p><cite>``start_join`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#start_join">https://www.consul.io/docs/agent/options.html#start_join</a>&gt;`_</p></li>
<li><p><cite>``start_join_wan`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#start_join_wan">https://www.consul.io/docs/agent/options.html#start_join_wan</a>&gt;`_</p></li>
<li><p><cite>``syslog_facility`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#syslog_facility">https://www.consul.io/docs/agent/options.html#syslog_facility</a>&gt;`_</p></li>
<li><p><cite>``tls_ca_file`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#ca_file">https://www.consul.io/docs/agent/options.html#ca_file</a>&gt;`_</p></li>
<li><p><cite>``tls_cert_file`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#cert_file">https://www.consul.io/docs/agent/options.html#cert_file</a>&gt;`_</p></li>
<li><p><cite>``tls_key_file`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#key_file">https://www.consul.io/docs/agent/options.html#key_file</a>&gt;`_</p></li>
<li><p><cite>``tls_min_version`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#tls_min_version">https://www.consul.io/docs/agent/options.html#tls_min_version</a>&gt;`_</p></li>
<li><p><cite>``tls_verify_incoming`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#verify_incoming">https://www.consul.io/docs/agent/options.html#verify_incoming</a>&gt;`_</p></li>
<li><p><cite>``tls_verify_outgoing`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#verify_outgoing">https://www.consul.io/docs/agent/options.html#verify_outgoing</a>&gt;`_</p></li>
<li><p><cite>``tls_verify_server_hostname`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#verify_server_hostname">https://www.consul.io/docs/agent/options.html#verify_server_hostname</a>&gt;`_</p></li>
<li><p><cite>``tagged_addresses`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#translate_wan_addrs">https://www.consul.io/docs/agent/options.html#translate_wan_addrs</a>&gt;`_</p></li>
<li><p><cite>``telemetry`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#telemetry">https://www.consul.io/docs/agent/options.html#telemetry</a>&gt;`_ - A map
of telemetry configuration.</p></li>
<li><p><cite>``translate_wan_addrs`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#translate_wan_addrs">https://www.consul.io/docs/agent/options.html#translate_wan_addrs</a>&gt;`_</p></li>
<li><p><cite>``ui_dir`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#ui_dir">https://www.consul.io/docs/agent/options.html#ui_dir</a>&gt;`_</p></li>
<li><p><cite>``unix_sockets`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/options.html#unix_sockets">https://www.consul.io/docs/agent/options.html#unix_sockets</a>&gt;`_</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAgentSelfResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAgentSelfResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the Consul agent.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">version_prerelease</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version_revision</span></code></p></li>
</ul>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetAutopilotHealthResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetAutopilotHealthResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">failure_tolerance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetAutopilotHealthResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAutopilotHealth.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetAutopilotHealthResult.failure_tolerance">
<code class="sig-name descname">failure_tolerance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAutopilotHealthResult.failure_tolerance" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of redundant healthy servers that could fail
without causing an outage</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAutopilotHealthResult.healthy">
<code class="sig-name descname">healthy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAutopilotHealthResult.healthy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the server is healthy according to the current Autopilot
configuration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAutopilotHealthResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAutopilotHealthResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetAutopilotHealthResult.servers">
<code class="sig-name descname">servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetAutopilotHealthResult.servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of server health information. See below for details on the
available information.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetCatalogNodesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetCatalogNodesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetCatalogNodesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCatalogNodes.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetCatalogNodesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetCatalogNodesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetCatalogServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetCatalogServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetCatalogServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCatalogService.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetCatalogServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetCatalogServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetCatalogServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetCatalogServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetCatalogServicesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCatalogServices.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetCatalogServicesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetCatalogServicesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetKeyPrefixResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetKeyPrefixResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkey_collection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetKeyPrefixResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeyPrefix.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetKeyPrefixResult.datacenter">
<code class="sig-name descname">datacenter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetKeyPrefixResult.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter the keys are being read from.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetKeyPrefixResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetKeyPrefixResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetKeyPrefixResult.path_prefix">
<code class="sig-name descname">path_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetKeyPrefixResult.path_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>the common prefix shared by all keys being read.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">var.&lt;name&gt;</span></code> - For each name given, the corresponding attribute
has the value of the key.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetKeyPrefixResult.subkeys">
<code class="sig-name descname">subkeys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetKeyPrefixResult.subkeys" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of the subkeys and values is set if no <code class="docutils literal notranslate"><span class="pre">subkey</span></code>
block is provided.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetKeysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeys.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetKeysResult.datacenter">
<code class="sig-name descname">datacenter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetKeysResult.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter the keys are being read from.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">var.&lt;name&gt;</span></code> - For each name given, the corresponding attribute
has the value of the key.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetKeysResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetKeysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetNodesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetNodesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetNodesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNodes.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetNodesResult.datacenter">
<code class="sig-name descname">datacenter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetNodesResult.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter the keys are being read from to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetNodesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetNodesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetNodesResult.node_ids">
<code class="sig-name descname">node_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetNodesResult.node_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Consul node IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetNodesResult.node_names">
<code class="sig-name descname">node_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetNodesResult.node_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Consul node names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetNodesResult.nodes">
<code class="sig-name descname">nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetNodesResult.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of nodes and details about each Consul agent.  The list of
per-node attributes is detailed below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetServiceHealthResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetServiceHealthResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">near</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceHealth.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetServiceHealthResult.datacenter">
<code class="sig-name descname">datacenter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter in which the node is running.</p>
<ul class="simple">
<li><p><cite>``tagged_addresses`</cite> &lt;<a class="reference external" href="https://www.consul.io/docs/agent/http/catalog.html#TaggedAddresses">https://www.consul.io/docs/agent/http/catalog.html#TaggedAddresses</a>&gt;`_ -
List of explicit LAN and WAN IP addresses for the agent.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceHealthResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceHealthResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this health-check.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceHealthResult.near">
<code class="sig-name descname">near</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult.near" title="Permalink to this definition">¶</a></dt>
<dd><p>The node to which the result must be sorted to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceHealthResult.node_meta">
<code class="sig-name descname">node_meta</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult.node_meta" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of metadata to filter the nodes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceHealthResult.passing">
<code class="sig-name descname">passing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult.passing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to return only nodes with all checks in the
passing state.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceHealthResult.results">
<code class="sig-name descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of entries and details about each endpoint advertising a
service.  Each element in the list has three attributes: <code class="docutils literal notranslate"><span class="pre">node</span></code>, <code class="docutils literal notranslate"><span class="pre">service</span></code> and
<code class="docutils literal notranslate"><span class="pre">checks</span></code>.  The list of the attributes of each one is detailed below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceHealthResult.tag">
<code class="sig-name descname">tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceHealthResult.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tag used to filter the list.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetServiceResult.datacenter">
<code class="sig-name descname">datacenter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceResult.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter the keys are being read from to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceResult.services">
<code class="sig-name descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceResult.services" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of nodes and details about each endpoint advertising a
service.  Each element in the list is a map of attributes that correspond to
each individual node.  The list of per-node attributes is detailed below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServiceResult.tag">
<code class="sig-name descname">tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServiceResult.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tag used to filter the list of nodes in <code class="docutils literal notranslate"><span class="pre">service</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.GetServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">GetServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.GetServicesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServices.</p>
<dl class="py attribute">
<dt id="pulumi_consul.GetServicesResult.datacenter">
<code class="sig-name descname">datacenter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServicesResult.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter the keys are being read from to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.GetServicesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.GetServicesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_consul.Intention">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">Intention</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Intention" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://www.consul.io/docs/connect/intentions.html">Intentions</a> are used to define
rules for which services may connect to one another when using <a class="reference external" href="https://www.consul.io/docs/connect/index.html">Consul Connect</a>.</p>
<p>It is appropriate to either reference existing services or specify non-existent services
that will be created in the future when creating intentions. This resource can be used
in conjunction with the <code class="docutils literal notranslate"><span class="pre">.Service</span></code> datasource when referencing services
registered on nodes that have a running Consul agent.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The intention action. Must be one of <code class="docutils literal notranslate"><span class="pre">allow</span></code> or <code class="docutils literal notranslate"><span class="pre">deny</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional description that can be used by Consul
tooling, but is not used internally.</p></li>
<li><p><strong>destination_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the destination service for the intention. This
service does not have to exist.</p></li>
<li><p><strong>destination_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination
namespace of the intention.</p></li>
<li><p><strong>meta</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/value pairs that are opaque to Consul and are associated
with the intention.</p></li>
<li><p><strong>source_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the source service for the intention. This
service does not have to exist.</p></li>
<li><p><strong>source_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source namespace of the
intention.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.Intention.action">
<code class="sig-name descname">action</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Intention.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The intention action. Must be one of <code class="docutils literal notranslate"><span class="pre">allow</span></code> or <code class="docutils literal notranslate"><span class="pre">deny</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Intention.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Intention.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional description that can be used by Consul
tooling, but is not used internally.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Intention.destination_name">
<code class="sig-name descname">destination_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Intention.destination_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the destination service for the intention. This
service does not have to exist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Intention.destination_namespace">
<code class="sig-name descname">destination_namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Intention.destination_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination
namespace of the intention.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Intention.meta">
<code class="sig-name descname">meta</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Intention.meta" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/value pairs that are opaque to Consul and are associated
with the intention.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Intention.source_name">
<code class="sig-name descname">source_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Intention.source_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the source service for the intention. This
service does not have to exist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Intention.source_namespace">
<code class="sig-name descname">source_namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Intention.source_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The source namespace of the
intention.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.Intention.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_namespace</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Intention.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Intention resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The intention action. Must be one of <code class="docutils literal notranslate"><span class="pre">allow</span></code> or <code class="docutils literal notranslate"><span class="pre">deny</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional description that can be used by Consul
tooling, but is not used internally.</p></li>
<li><p><strong>destination_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the destination service for the intention. This
service does not have to exist.</p></li>
<li><p><strong>destination_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination
namespace of the intention.</p></li>
<li><p><strong>meta</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/value pairs that are opaque to Consul and are associated
with the intention.</p></li>
<li><p><strong>source_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the source service for the intention. This
service does not have to exist.</p></li>
<li><p><strong>source_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source namespace of the
intention.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.Intention.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Intention.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Intention.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Intention.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.KeyPrefix">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">KeyPrefix</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkey_collection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.KeyPrefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KeyPrefix resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] datacenter: The datacenter to use. This overrides the</p>
<blockquote>
<div><p>agent’s default datacenter and the datacenter in the provider setup.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the keys within.</p></li>
<li><p><strong>path_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the common prefix shared by all keys
that will be managed by this resource instance. In most cases this will
end with a slash, to manage a “folder” of keys.</p></li>
<li><p><strong>subkey_collection</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A subkey to add. Supported values documented below.
Multiple blocks supported.</p></li>
<li><p><strong>subkeys</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping from subkey name (which will be appended
to the given <code class="docutils literal notranslate"><span class="pre">path_prefix</span></code>) to the value that should be stored at that key.
Use slashes, as shown in the above example, to create “sub-folders” under
the given path prefix.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ACL token to use. This overrides the
token that the agent provides by default.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>subkey_collection</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An <a class="reference external" href="https://www.consul.io/api/kv.html#flags-1">unsigned integer value</a>
to attach to the key (defaults to 0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This is the path (which will be appended to the given
<code class="docutils literal notranslate"><span class="pre">path_prefix</span></code>) in Consul that should be written to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to write to the given path.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_consul.KeyPrefix.datacenter">
<code class="sig-name descname">datacenter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.KeyPrefix.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.KeyPrefix.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.KeyPrefix.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace to create the keys within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.KeyPrefix.path_prefix">
<code class="sig-name descname">path_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.KeyPrefix.path_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the common prefix shared by all keys
that will be managed by this resource instance. In most cases this will
end with a slash, to manage a “folder” of keys.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.KeyPrefix.subkey_collection">
<code class="sig-name descname">subkey_collection</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.KeyPrefix.subkey_collection" title="Permalink to this definition">¶</a></dt>
<dd><p>A subkey to add. Supported values documented below.
Multiple blocks supported.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - An <a class="reference external" href="https://www.consul.io/api/kv.html#flags-1">unsigned integer value</a>
to attach to the key (defaults to 0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the path (which will be appended to the given
<code class="docutils literal notranslate"><span class="pre">path_prefix</span></code>) in Consul that should be written to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to write to the given path.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.KeyPrefix.subkeys">
<code class="sig-name descname">subkeys</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.KeyPrefix.subkeys" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping from subkey name (which will be appended
to the given <code class="docutils literal notranslate"><span class="pre">path_prefix</span></code>) to the value that should be stored at that key.
Use slashes, as shown in the above example, to create “sub-folders” under
the given path prefix.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.KeyPrefix.token">
<code class="sig-name descname">token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.KeyPrefix.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The ACL token to use. This overrides the
token that the agent provides by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.KeyPrefix.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkey_collection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.KeyPrefix.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyPrefix resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the keys within.</p></li>
<li><p><strong>path_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the common prefix shared by all keys
that will be managed by this resource instance. In most cases this will
end with a slash, to manage a “folder” of keys.</p></li>
<li><p><strong>subkey_collection</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A subkey to add. Supported values documented below.
Multiple blocks supported.</p></li>
<li><p><strong>subkeys</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping from subkey name (which will be appended
to the given <code class="docutils literal notranslate"><span class="pre">path_prefix</span></code>) to the value that should be stored at that key.
Use slashes, as shown in the above example, to create “sub-folders” under
the given path prefix.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ACL token to use. This overrides the
token that the agent provides by default.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>subkey_collection</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An <a class="reference external" href="https://www.consul.io/api/kv.html#flags-1">unsigned integer value</a>
to attach to the key (defaults to 0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This is the path (which will be appended to the given
<code class="docutils literal notranslate"><span class="pre">path_prefix</span></code>) in Consul that should be written to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to write to the given path.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.KeyPrefix.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.KeyPrefix.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.KeyPrefix.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.KeyPrefix.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Keys">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">Keys</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Keys resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] datacenter: The datacenter to use. This overrides the</p>
<blockquote>
<div><p>agent’s default datacenter and the datacenter in the provider setup.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a key in Consul to be written.
Supported values documented below.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the keys within.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ACL token to use. This overrides the
token that the agent provides by default.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, then the key will be deleted when
either its configuration block is removed from the configuration or
the entire resource is destroyed. Otherwise, it will be left in Consul.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An <a class="reference external" href="https://www.consul.io/api/kv.html#flags-1">unsigned integer value</a>
to attach to the key (defaults to 0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This is the path in Consul that should be written to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to write to the given path.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_consul.Keys.datacenter">
<code class="sig-name descname">datacenter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Keys.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Keys.keys">
<code class="sig-name descname">keys</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Keys.keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a key in Consul to be written.
Supported values documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, then the key will be deleted when
either its configuration block is removed from the configuration or
the entire resource is destroyed. Otherwise, it will be left in Consul.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - An <a class="reference external" href="https://www.consul.io/api/kv.html#flags-1">unsigned integer value</a>
to attach to the key (defaults to 0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the path in Consul that should be written to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to write to the given path.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Keys.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Keys.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace to create the keys within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Keys.token">
<code class="sig-name descname">token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Keys.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The ACL token to use. This overrides the
token that the agent provides by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.Keys.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Keys.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Keys resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a key in Consul to be written.
Supported values documented below.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the keys within.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ACL token to use. This overrides the
token that the agent provides by default.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, then the key will be deleted when
either its configuration block is removed from the configuration or
the entire resource is destroyed. Otherwise, it will be left in Consul.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An <a class="reference external" href="https://www.consul.io/api/kv.html#flags-1">unsigned integer value</a>
to attach to the key (defaults to 0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This is the path in Consul that should be written to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to write to the given path.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.Keys.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Keys.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Keys.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Keys.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Node">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">Node</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Node" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to Node data in Consul. This can be used to define a
node. Currently, defining health checks is not supported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the node being added to,
or referenced in the catalog.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the agent’s
default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>meta</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/value pairs that are associated with the node.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node being added to, or
referenced in the catalog.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_consul.Node.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Node.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The address of the node being added to,
or referenced in the catalog.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Node.datacenter">
<code class="sig-name descname">datacenter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Node.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter to use. This overrides the agent’s
default datacenter and the datacenter in the provider setup.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Node.meta">
<code class="sig-name descname">meta</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Node.meta" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/value pairs that are associated with the node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Node.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Node.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the node being added to, or
referenced in the catalog.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.Node.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Node.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Node resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the node being added to,
or referenced in the catalog.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the agent’s
default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>meta</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/value pairs that are associated with the node.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node being added to, or
referenced in the catalog.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.Node.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Node.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Node.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Node.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.PreparedQuery">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">PreparedQuery</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">failover</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">near</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_passing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stored_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.PreparedQuery" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PreparedQuery resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] connect: When <code class="docutils literal notranslate"><span class="pre">true</span></code> the prepared query will return connect</p>
<blockquote>
<div><p>proxy services for a queried service.  Conditions such as <code class="docutils literal notranslate"><span class="pre">tags</span></code> in the
prepared query will be matched against the proxy service. Defaults to false.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings for controlling the DNS response details.</p></li>
<li><p><strong>failover</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options for controlling behavior when no healthy
nodes are available in the local DC.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the prepared query. Used to identify
the prepared query during requests. Can be specified as an empty string
to configure the query as a catch-all.</p></li>
<li><p><strong>near</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allows specifying the name of a node to sort results
near using Consul’s distance sorting and network coordinates. The magic
<code class="docutils literal notranslate"><span class="pre">_agent</span></code> value can be used to always sort nearest the node servicing the
request.</p></li>
<li><p><strong>only_passing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the prepared query will only
return nodes with passing health checks in the result.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service to query.</p></li>
<li><p><strong>session</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Consul session to tie this query’s
lifetime to.  This is an advanced parameter that should not be used without a
complete understanding of Consul sessions and the implications of their use
(it is recommended to leave this blank in nearly all cases).  If this
parameter is omitted the query will not expire.</p></li>
<li><p><strong>stored_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ACL token to store with the prepared
query. This token will be used by default whenever the query is executed.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of required and/or disallowed tags.  If a tag is
in this list it must be present.  If the tag is preceded with a “!” then it is
disallowed.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Query templating options. This is used to make a
single prepared query respond to many different requests.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ACL token to use when saving the prepared query.
This overrides the token that the agent provides by default.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The TTL to send when returning DNS results.</p></li>
</ul>
<p>The <strong>failover</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Remote datacenters to return results from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nearestN</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Return results from this many datacenters,
sorted in ascending order of estimated RTT.</p></li>
</ul>
<p>The <strong>template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regexp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The regular expression to match with. When using
<code class="docutils literal notranslate"><span class="pre">name_prefix_match</span></code>, this regex is applied against the query name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of template matching to perform. Currently
only <code class="docutils literal notranslate"><span class="pre">name_prefix_match</span></code> is supported.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.connect">
<code class="sig-name descname">connect</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.connect" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code> the prepared query will return connect
proxy services for a queried service.  Conditions such as <code class="docutils literal notranslate"><span class="pre">tags</span></code> in the
prepared query will be matched against the proxy service. Defaults to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.datacenter">
<code class="sig-name descname">datacenter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.dns">
<code class="sig-name descname">dns</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.dns" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings for controlling the DNS response details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The TTL to send when returning DNS results.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.failover">
<code class="sig-name descname">failover</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.failover" title="Permalink to this definition">¶</a></dt>
<dd><p>Options for controlling behavior when no healthy
nodes are available in the local DC.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Remote datacenters to return results from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nearestN</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Return results from this many datacenters,
sorted in ascending order of estimated RTT.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the prepared query. Used to identify
the prepared query during requests. Can be specified as an empty string
to configure the query as a catch-all.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.near">
<code class="sig-name descname">near</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.near" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows specifying the name of a node to sort results
near using Consul’s distance sorting and network coordinates. The magic
<code class="docutils literal notranslate"><span class="pre">_agent</span></code> value can be used to always sort nearest the node servicing the
request.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.only_passing">
<code class="sig-name descname">only_passing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.only_passing" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the prepared query will only
return nodes with passing health checks in the result.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service to query.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.session">
<code class="sig-name descname">session</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.session" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Consul session to tie this query’s
lifetime to.  This is an advanced parameter that should not be used without a
complete understanding of Consul sessions and the implications of their use
(it is recommended to leave this blank in nearly all cases).  If this
parameter is omitted the query will not expire.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.stored_token">
<code class="sig-name descname">stored_token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.stored_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The ACL token to store with the prepared
query. This token will be used by default whenever the query is executed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of required and/or disallowed tags.  If a tag is
in this list it must be present.  If the tag is preceded with a “!” then it is
disallowed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.template">
<code class="sig-name descname">template</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.template" title="Permalink to this definition">¶</a></dt>
<dd><p>Query templating options. This is used to make a
single prepared query respond to many different requests.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regexp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The regular expression to match with. When using
<code class="docutils literal notranslate"><span class="pre">name_prefix_match</span></code>, this regex is applied against the query name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of template matching to perform. Currently
only <code class="docutils literal notranslate"><span class="pre">name_prefix_match</span></code> is supported.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.PreparedQuery.token">
<code class="sig-name descname">token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.PreparedQuery.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The ACL token to use when saving the prepared query.
This overrides the token that the agent provides by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.PreparedQuery.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">failover</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">near</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_passing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stored_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.PreparedQuery.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PreparedQuery resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connect</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code> the prepared query will return connect
proxy services for a queried service.  Conditions such as <code class="docutils literal notranslate"><span class="pre">tags</span></code> in the
prepared query will be matched against the proxy service. Defaults to false.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings for controlling the DNS response details.</p></li>
<li><p><strong>failover</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options for controlling behavior when no healthy
nodes are available in the local DC.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the prepared query. Used to identify
the prepared query during requests. Can be specified as an empty string
to configure the query as a catch-all.</p></li>
<li><p><strong>near</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allows specifying the name of a node to sort results
near using Consul’s distance sorting and network coordinates. The magic
<code class="docutils literal notranslate"><span class="pre">_agent</span></code> value can be used to always sort nearest the node servicing the
request.</p></li>
<li><p><strong>only_passing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the prepared query will only
return nodes with passing health checks in the result.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service to query.</p></li>
<li><p><strong>session</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Consul session to tie this query’s
lifetime to.  This is an advanced parameter that should not be used without a
complete understanding of Consul sessions and the implications of their use
(it is recommended to leave this blank in nearly all cases).  If this
parameter is omitted the query will not expire.</p></li>
<li><p><strong>stored_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ACL token to store with the prepared
query. This token will be used by default whenever the query is executed.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of required and/or disallowed tags.  If a tag is
in this list it must be present.  If the tag is preceded with a “!” then it is
disallowed.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Query templating options. This is used to make a
single prepared query respond to many different requests.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ACL token to use when saving the prepared query.
This overrides the token that the agent provides by default.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The TTL to send when returning DNS results.</p></li>
</ul>
<p>The <strong>failover</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Remote datacenters to return results from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nearestN</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Return results from this many datacenters,
sorted in ascending order of estimated RTT.</p></li>
</ul>
<p>The <strong>template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regexp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The regular expression to match with. When using
<code class="docutils literal notranslate"><span class="pre">name_prefix_match</span></code>, this regex is applied against the query name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of template matching to perform. Currently
only <code class="docutils literal notranslate"><span class="pre">name_prefix_match</span></code> is supported.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.PreparedQuery.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.PreparedQuery.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.PreparedQuery.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.PreparedQuery.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure_https</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the consul package. By default, resources use package-wide configuration
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
<dt id="pulumi_consul.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">checks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>A high-level resource for creating a Service in Consul in the Consul catalog. This
is appropriate for registering <a class="reference external" href="https://www.consul.io/docs/guides/external.html">external services</a> and
can be used to create services addressable by Consul that cannot be registered
with a <a class="reference external" href="https://www.consul.io/docs/agent/basics.html">local agent</a>.</p>
<p>If the Consul agent is running on the node where this service is registered, it is
not recommended to use this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the service. Defaults to the
address of the node.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>meta</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of arbitrary KV metadata linked to the service
instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the health-check.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the service within.</p></li>
<li><p><strong>node</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node the to register the service on.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port of the service.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>If the service ID is not provided, it will be defaulted to the value</p></li>
</ul>
<p>of the <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>checks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An ID, <em>unique per agent</em>. Will default to <em>name</em>
if not set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deregisterCriticalServiceAfter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time after which
the service is automatically deregistered when in the <code class="docutils literal notranslate"><span class="pre">critical</span></code> state.
Defaults to <code class="docutils literal notranslate"><span class="pre">30s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The headers to send for an HTTP check.
The attributes of each header is given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The header’s list of values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">http</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP endpoint to call for an HTTP check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The interval to wait between each health-check
invocation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The method to use for HTTP health-checks. Defaults
to <code class="docutils literal notranslate"><span class="pre">GET</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the health-check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An opaque field meant to hold human readable text.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The initial health-check status.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The TCP address and port to connect to for a TCP check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The timeout value for HTTP checks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsSkipVerify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to deactivate certificate
verification for HTTP health-checks. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_consul.Service.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The address of the service. Defaults to the
address of the node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Service.datacenter">
<code class="sig-name descname">datacenter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Service.meta">
<code class="sig-name descname">meta</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.meta" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of arbitrary KV metadata linked to the service
instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Service.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the health-check.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Service.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace to create the service within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Service.node">
<code class="sig-name descname">node</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.node" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the node the to register the service on.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Service.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port of the service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Service.service_id">
<code class="sig-name descname">service_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.service_id" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>If the service ID is not provided, it will be defaulted to the value
of the <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_consul.Service.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_consul.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">checks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address of the service. Defaults to the
address of the node.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>meta</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of arbitrary KV metadata linked to the service
instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the health-check.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace to create the service within.</p></li>
<li><p><strong>node</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node the to register the service on.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port of the service.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>If the service ID is not provided, it will be defaulted to the value</p></li>
</ul>
<p>of the <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>checks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An ID, <em>unique per agent</em>. Will default to <em>name</em>
if not set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deregisterCriticalServiceAfter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time after which
the service is automatically deregistered when in the <code class="docutils literal notranslate"><span class="pre">critical</span></code> state.
Defaults to <code class="docutils literal notranslate"><span class="pre">30s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The headers to send for an HTTP check.
The attributes of each header is given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The header’s list of values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">http</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP endpoint to call for an HTTP check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The interval to wait between each health-check
invocation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The method to use for HTTP health-checks. Defaults
to <code class="docutils literal notranslate"><span class="pre">GET</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the health-check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An opaque field meant to hold human readable text.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The initial health-check status.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The TCP address and port to connect to for a TCP check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The timeout value for HTTP checks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsSkipVerify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to deactivate certificate
verification for HTTP health-checks. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_consul.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_consul.get_acl_auth_method">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_acl_auth_method</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_acl_auth_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.AclAuthMethod</span></code> data source returns the information related to a
<a class="reference external" href="https://www.consul.io/docs/acl/acl-auth-methods.html">Consul Auth Method</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config</strong> (<em>dict</em>) – The configuration options of the ACL Auth Method.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – The description of the ACL Auth Method.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the ACL Auth Method.</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – The namespace to lookup the auth method.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The type of the ACL Auth Method.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_acl_policy">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_acl_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_acl_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.AclPolicy</span></code> data source returns the information related to a
<a class="reference external" href="https://www.consul.io/docs/acl/acl-system.html#acl-policies">Consul ACL Policy</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>datacenters</strong> (<em>list</em>) – The datacenters associated with the ACL Policy.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – The description of the ACL Policy.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the ACL Policy.</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – The namespace to lookup the policy.</p></li>
<li><p><strong>rules</strong> (<em>str</em>) – The rules associated with the ACL Policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_acl_role">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_acl_role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_acl_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.AclRole</span></code> data source returns the information related to a
<a class="reference external" href="https://www.consul.io/api/acl/roles.html">Consul ACL Role</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – The description of the ACL Role.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the ACL Role.</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – The namespace to lookup the role.</p></li>
<li><p><strong>policies</strong> (<em>list</em>) – The list of policies associated with the ACL Role. Each entry has
an <code class="docutils literal notranslate"><span class="pre">id</span></code> and a <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute.</p></li>
<li><p><strong>service_identities</strong> (<em>list</em>) – The list of service identities associated with the ACL
Role. Each entry has a <code class="docutils literal notranslate"><span class="pre">service_name</span></code> attribute and a list of <code class="docutils literal notranslate"><span class="pre">datacenters</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the ACL Role.</p></li>
</ul>
<p>The <strong>service_identities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_acl_token">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_acl_token</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accessor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_acl_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.AclToken</span></code> data source returns the information related to the
<code class="docutils literal notranslate"><span class="pre">.AclToken</span></code> resource with the exception of its secret ID.</p>
<p>If you want to get the secret ID associated with a token, use the
<cite>`</cite>.getAclTokenSecretId`` data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/consul/d/acl_token_secret_id.html">https://www.terraform.io/docs/providers/consul/d/acl_token_secret_id.html</a>&gt;`_.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>accessor_id</strong> (<em>str</em>) – The accessor ID of the ACL token.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – The description of the ACL token.</p></li>
<li><p><strong>local</strong> (<em>bool</em>) – Whether the ACL token is local to the datacenter it was created within.</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – The namespace to lookup the ACL token.</p></li>
<li><p><strong>policies</strong> (<em>list</em>) – A list of policies associated with the ACL token. Each entry has
an <code class="docutils literal notranslate"><span class="pre">id</span></code> and a <code class="docutils literal notranslate"><span class="pre">name</span></code> attribute.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_acl_token_secret_id">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_acl_token_secret_id</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accessor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_acl_token_secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>accessor_id</strong> (<em>str</em>) – The accessor ID of the ACL token.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_agent_config">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_agent_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_agent_config" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>Note:</strong> The <code class="docutils literal notranslate"><span class="pre">.getAgentConfig</span></code> resource differs from <cite>`</cite>.getAgentSelf`` &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/consul/d/agent_self.html">https://www.terraform.io/docs/providers/consul/d/agent_self.html</a>&gt;`_,
providing less information but utilizing stable APIs. <code class="docutils literal notranslate"><span class="pre">.getAgentSelf</span></code> will be
deprecated in a future release.</p>
</div></blockquote>
<p>The <code class="docutils literal notranslate"><span class="pre">.getAgentConfig</span></code> data source returns
<a class="reference external" href="https://www.consul.io/api/agent.html#read-configuration">configuration data</a>
from the agent specified in the <code class="docutils literal notranslate"><span class="pre">provider</span></code>.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_agent_self">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_agent_self</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_agent_self" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>Warning:</strong> The <code class="docutils literal notranslate"><span class="pre">.getAgentSelf</span></code> resource has been deprecated and will be removed
from a future release of the provider. Read the <a class="reference external" href="https://www.terraform.io/docs/providers/consul/guides/upgrading.html#deprecation-of-consul_agent_self">upgrade instructions</a> for more information.</p>
</div></blockquote>
<p>The <code class="docutils literal notranslate"><span class="pre">.getAgentSelf</span></code> data source returns
<a class="reference external" href="https://www.consul.io/docs/agent/http/agent.html#agent_self">configuration and status data</a>
from the agent specified in the <code class="docutils literal notranslate"><span class="pre">provider</span></code>.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_autopilot_health">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_autopilot_health</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_autopilot_health" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.getAutopilotHealth</span></code> data source returns
<a class="reference external" href="https://www.consul.io/api/operator/autopilot.html#read-health">autopilot health information</a>
about the current Consul cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>datacenter</strong> (<em>str</em>) – The datacenter to use. This overrides the agent’s
default datacenter and the datacenter in the provider setup.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_catalog_nodes">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_catalog_nodes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_catalog_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<p>The <strong>query_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowStale</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">near</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMeta</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireConsistent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_catalog_service">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_catalog_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_catalog_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<p>The <strong>query_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowStale</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">near</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMeta</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireConsistent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_catalog_services">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_catalog_services</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_catalog_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<p>The <strong>query_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowStale</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">near</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMeta</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireConsistent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_key_prefix">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_key_prefix</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subkey_collection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_key_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>datacenter</strong> (<em>str</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – The namespace to create the keys within.</p></li>
<li><p><strong>path_prefix</strong> (<em>str</em>) – Specifies the common prefix shared by all keys
that will be read by this data source instance. In most cases, this will
end with a slash to read a “folder” of subkeys.</p></li>
<li><p><strong>subkey_collection</strong> (<em>list</em>) – Specifies a subkey in Consul to be read. Supported
values documented below. Multiple blocks supported.</p></li>
<li><p><strong>token</strong> (<em>str</em>) – The ACL token to use. This overrides the
token that the agent provides by default.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>subkey_collection</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the default value to set for <code class="docutils literal notranslate"><span class="pre">var.&lt;name&gt;</span></code>
if the key does not exist in Consul. Defaults to an empty string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the name of the key. This value of the
key is exposed as <code class="docutils literal notranslate"><span class="pre">var.&lt;name&gt;</span></code>. This is not the path of the subkey
in Consul.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the subkey path in Consul (which will be appended
to the given <code class="docutils literal notranslate"><span class="pre">path_prefix</span></code>) to construct the full key that will be used
to read the value.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_keys">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_keys</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Keys</span></code> resource reads values from the Consul key/value store.
This is a powerful way dynamically set values in templates.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>datacenter</strong> (<em>str</em>) – The datacenter to use. This overrides the
agent’s default datacenter and the datacenter in the provider setup.</p></li>
<li><p><strong>keys</strong> (<em>list</em>) – Specifies a key in Consul to be read. Supported
values documented below. Multiple blocks supported.</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – The namespace to lookup the keys.</p></li>
<li><p><strong>token</strong> (<em>str</em>) – The ACL token to use. This overrides the
token that the agent provides by default.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the default value to set for <code class="docutils literal notranslate"><span class="pre">var.&lt;name&gt;</span></code>
if the key does not exist in Consul. Defaults to an empty string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the name of the key. This value of the
key is exposed as <code class="docutils literal notranslate"><span class="pre">var.&lt;name&gt;</span></code>. This is not the path of the key
in Consul.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the path in Consul that should be read
or written to.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_nodes">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_nodes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.getNodes</span></code> data source returns a list of Consul nodes that have
been registered with the Consul cluster in a given datacenter.  By specifying a
different datacenter in the <code class="docutils literal notranslate"><span class="pre">query_options</span></code> it is possible to retrieve a list of
nodes from a different WAN-attached Consul datacenter.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>query_options</strong> (<em>list</em>) – See below.</p>
</dd>
</dl>
<p>The <strong>query_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowStale</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the default, allow responses from
Consul servers that are followers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Consul datacenter to query.  Defaults to the
same value found in <code class="docutils literal notranslate"><span class="pre">query_options</span></code> parameter specified below, or if that is
empty, the <code class="docutils literal notranslate"><span class="pre">datacenter</span></code> value found in the Consul agent that this provider is
configured to talk to then the datacenter in the provider setup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">near</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMeta</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireConsistent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code> force the client to perform a
read on at least quorum servers and verify the result is the same.  Defaults
to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specify the Consul ACL token to use when performing the
request.  This defaults to the same API token configured by the <code class="docutils literal notranslate"><span class="pre">consul</span></code>
provider but may be overriden if necessary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Index number used to enable blocking quereis.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Max time the client should wait for a blocking query
to return.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_service">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Service</span></code> provides details about a specific Consul service in a
given datacenter.  The results include a list of nodes advertising the specified
service, the node’s IP address, port number, node ID, etc.  By specifying a
different datacenter in the <code class="docutils literal notranslate"><span class="pre">query_options</span></code> it is possible to retrieve a list of
services from a different WAN-attached Consul datacenter.</p>
<p>This data source is different from the <code class="docutils literal notranslate"><span class="pre">.getServices</span></code> (plural) data
source, which provides a summary of the current Consul services.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>datacenter</strong> (<em>str</em>) – The Consul datacenter to query.  Defaults to the
same value found in <code class="docutils literal notranslate"><span class="pre">query_options</span></code> parameter specified below, or if that is
empty, the <code class="docutils literal notranslate"><span class="pre">datacenter</span></code> value found in the Consul agent that this provider is
configured to talk to.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The service name to select.</p></li>
<li><p><strong>query_options</strong> (<em>list</em>) – See below.</p></li>
<li><p><strong>tag</strong> (<em>str</em>) – A single tag that can be used to filter the list of nodes
to return based on a single matching tag..</p></li>
</ul>
</dd>
</dl>
<p>The <strong>query_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowStale</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the default, allow responses from
Consul servers that are followers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Consul datacenter to query.  Defaults to the
same value found in <code class="docutils literal notranslate"><span class="pre">query_options</span></code> parameter specified below, or if that is
empty, the <code class="docutils literal notranslate"><span class="pre">datacenter</span></code> value found in the Consul agent that this provider is
configured to talk to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The namespace to lookup the service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">near</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMeta</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireConsistent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code> force the client to perform a
read on at least quorum servers and verify the result is the same.  Defaults
to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specify the Consul ACL token to use when performing the
request.  This defaults to the same API token configured by the <code class="docutils literal notranslate"><span class="pre">consul</span></code>
provider but may be overriden if necessary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Index number used to enable blocking quereis.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Max time the client should wait for a blocking query
to return.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_service_health">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_service_health</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">near</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_service_health" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getServiceHealth</span></code> can be used to get the list of the instances that
are currently healthy, according to their associated  health-checks.
The result includes the list of service instances, the node associated to each
instance and its health-checks.</p>
<p>This resource is likely to change as frequently as the health-checks are being
updated, you should expect different results in a frequent basis.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>datacenter</strong> (<em>str</em>) – The Consul datacenter to query.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The service name to select.</p></li>
<li><p><strong>near</strong> (<em>str</em>) – Specifies a node name to sort the node list in ascending order
based on the estimated round trip time from that node.</p></li>
<li><p><strong>node_meta</strong> (<em>dict</em>) – Filter the results to nodes with the specified key/value
pairs.</p></li>
<li><p><strong>passing</strong> (<em>bool</em>) – Whether to return only nodes with all checks in the
passing state. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>tag</strong> (<em>str</em>) – A single tag that can be used to filter the list to return
based on a single matching tag.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_consul.get_services">
<code class="sig-prename descclassname">pulumi_consul.</code><code class="sig-name descname">get_services</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">query_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_consul.get_services" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.getServices</span></code> data source returns a list of Consul services that
have been registered with the Consul cluster in a given datacenter.  By
specifying a different datacenter in the <code class="docutils literal notranslate"><span class="pre">query_options</span></code> it is possible to
retrieve a list of services from a different WAN-attached Consul datacenter.</p>
<p>This data source is different from the <code class="docutils literal notranslate"><span class="pre">.Service</span></code> (singular) data
source, which provides a detailed response about a specific Consul service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>query_options</strong> (<em>list</em>) – See below.</p>
</dd>
</dl>
<p>The <strong>query_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowStale</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the default, allow responses from
Consul servers that are followers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Consul datacenter to query.  Defaults to the
same value found in <code class="docutils literal notranslate"><span class="pre">query_options</span></code> parameter specified below, or if that is
empty, the <code class="docutils literal notranslate"><span class="pre">datacenter</span></code> value found in the Consul agent that this provider is
configured to talk to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The namespace to lookup the services.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">near</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMeta</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireConsistent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code> force the client to perform a
read on at least quorum servers and verify the result is the same.  Defaults
to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specify the Consul ACL token to use when performing the
request.  This defaults to the same API token configured by the <code class="docutils literal notranslate"><span class="pre">consul</span></code>
provider but may be overriden if necessary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Index number used to enable blocking quereis.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Max time the client should wait for a blocking query
to return.</p></li>
</ul>
</dd></dl>

</div>
