---
title: Module managementresource
title_tag: Module managementresource | Package pulumi_azure | Python SDK
linktitle: managementresource
notitle: true
---

<div class="section" id="managementresource">
<h1>managementresource<a class="headerlink" href="#managementresource" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.managementresource"></span><dl class="class">
<dt id="pulumi_azure.managementresource.ManangementLock">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.managementresource.</code><code class="sig-name descname">ManangementLock</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">lock_level=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notes=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementresource.ManangementLock" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Management Lock which is scoped to a Subscription, Resource Group or Resource.</p>
<p>Deprecated: azure.ManangementLock has been deprecated in favour of azure.Lock</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>lock_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Level to be used for this Lock. Possible values are <code class="docutils literal notranslate"><span class="pre">CanNotDelete</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Management Lock. Changing this forces a new resource to be created.</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies some notes about the lock. Maximum of 512 characters. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope at which the Management Lock should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.managementresource.ManangementLock.lock_level">
<code class="sig-name descname">lock_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementresource.ManangementLock.lock_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Level to be used for this Lock. Possible values are <code class="docutils literal notranslate"><span class="pre">CanNotDelete</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementresource.ManangementLock.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementresource.ManangementLock.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Management Lock. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementresource.ManangementLock.notes">
<code class="sig-name descname">notes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementresource.ManangementLock.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies some notes about the lock. Maximum of 512 characters. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementresource.ManangementLock.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementresource.ManangementLock.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the scope at which the Management Lock should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.managementresource.ManangementLock.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">lock_level=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notes=None</em>, <em class="sig-param">scope=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementresource.ManangementLock.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManangementLock resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>lock_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Level to be used for this Lock. Possible values are <code class="docutils literal notranslate"><span class="pre">CanNotDelete</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Management Lock. Changing this forces a new resource to be created.</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies some notes about the lock. Maximum of 512 characters. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope at which the Management Lock should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.managementresource.ManangementLock.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementresource.ManangementLock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.managementresource.ManangementLock.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementresource.ManangementLock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
