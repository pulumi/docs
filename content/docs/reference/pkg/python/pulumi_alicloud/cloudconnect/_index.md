---
title: Module cloudconnect
title_tag: Module cloudconnect | Package pulumi_alicloud | Python SDK
linktitle: cloudconnect
notitle: true
---

<div class="section" id="cloudconnect">
<h1>cloudconnect<a class="headerlink" href="#cloudconnect" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cloudconnect"></span><dl class="py class">
<dt id="pulumi_alicloud.cloudconnect.AwaitableGetNetworksResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cloudconnect.</code><code class="sig-name descname">AwaitableGetNetworksResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.AwaitableGetNetworksResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cloudconnect.GetNetworksResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cloudconnect.</code><code class="sig-name descname">GetNetworksResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.GetNetworksResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworks.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.GetNetworksResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.GetNetworksResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.GetNetworksResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.GetNetworksResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CCN instances IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.GetNetworksResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.GetNetworksResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CCN instances names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.GetNetworksResult.networks">
<code class="sig-name descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.GetNetworksResult.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CCN instances. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cloudconnect.Network">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cloudconnect.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a cloud connect network resource. Cloud Connect Network (CCN) is another important component of Smart Access Gateway. It is a device access matrix composed of Alibaba Cloud distributed access gateways. You can add multiple Smart Access Gateway (SAG) devices to a CCN instance and then attach the CCN instance to a Cloud Enterprise Network (CEN) instance to connect the local branches to the Alibaba Cloud.</p>
<p>For information about cloud connect network and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/93667.htm">What is Cloud Connect Network</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.59.0+</p>
<p><strong>NOTE:</strong> Only the following regions support create Cloud Connect Network. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CidrBlock of the CCN instance. Defaults to null.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the CCN instance. The description can contain 2 to 256 characters. The description must start with English letters, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>is_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Created by default. If the client does not have ccn in the binding, it will create a ccn for the user to replace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CCN instance. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.Network.cidr_block">
<code class="sig-name descname">cidr_block</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.Network.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CidrBlock of the CCN instance. Defaults to null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.Network.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.Network.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the CCN instance. The description can contain 2 to 256 characters. The description must start with English letters, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.Network.is_default">
<code class="sig-name descname">is_default</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.Network.is_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Created by default. If the client does not have ccn in the binding, it will create a ccn for the user to replace.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.Network.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.Network.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the CCN instance. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cloudconnect.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.Network.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CidrBlock of the CCN instance. Defaults to null.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the CCN instance. The description can contain 2 to 256 characters. The description must start with English letters, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>is_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Created by default. If the client does not have ccn in the binding, it will create a ccn for the user to replace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CCN instance. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cloudconnect.Network.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.Network.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cloudconnect.Network.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.Network.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cloudconnect.NetworkAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cloudconnect.</code><code class="sig-name descname">NetworkAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ccn_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sag_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloud Connect Network Attachment resource. This topic describes how to associate a Smart Access Gateway (SAG) instance with a network instance. You must associate an SAG instance with a network instance if you want to connect the SAG to Alibaba Cloud. You can connect an SAG to Alibaba Cloud through a leased line, the Internet, or the active and standby links.</p>
<p>For information about Cloud Connect Network Attachment and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/124230.htm">What is Cloud Connect Network Attachment</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.64.0+</p>
<p><strong>NOTE:</strong> Only the following regions support. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ccn_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CCN instance.</p></li>
<li><p><strong>sag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Smart Access Gateway instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.NetworkAttachment.ccn_id">
<code class="sig-name descname">ccn_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkAttachment.ccn_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CCN instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.NetworkAttachment.sag_id">
<code class="sig-name descname">sag_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkAttachment.sag_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Smart Access Gateway instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cloudconnect.NetworkAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ccn_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sag_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ccn_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CCN instance.</p></li>
<li><p><strong>sag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Smart Access Gateway instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cloudconnect.NetworkAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cloudconnect.NetworkAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cloudconnect.NetworkGrant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cloudconnect.</code><code class="sig-name descname">NetworkGrant</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ccn_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cen_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cen_uid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkGrant" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloud Connect Network Grant resource. If the CEN instance to be attached belongs to another account, authorization by the CEN instance is required.</p>
<p>For information about Cloud Connect Network Grant and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/94543.htm">What is Cloud Connect Network Grant</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.63.0+</p>
<p><strong>NOTE:</strong> Only the following regions support create Cloud Connect Network Grant. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ccn_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CCN instance.</p></li>
<li><p><strong>cen_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN instance.</p></li>
<li><p><strong>cen_uid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account to which the CEN instance belongs.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.NetworkGrant.ccn_id">
<code class="sig-name descname">ccn_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkGrant.ccn_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CCN instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.NetworkGrant.cen_id">
<code class="sig-name descname">cen_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkGrant.cen_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CEN instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cloudconnect.NetworkGrant.cen_uid">
<code class="sig-name descname">cen_uid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkGrant.cen_uid" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the account to which the CEN instance belongs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cloudconnect.NetworkGrant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ccn_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cen_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cen_uid</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkGrant.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkGrant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ccn_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CCN instance.</p></li>
<li><p><strong>cen_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN instance.</p></li>
<li><p><strong>cen_uid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account to which the CEN instance belongs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cloudconnect.NetworkGrant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkGrant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cloudconnect.NetworkGrant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.NetworkGrant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cloudconnect.get_networks">
<code class="sig-prename descclassname">pulumi_alicloud.cloudconnect.</code><code class="sig-name descname">get_networks</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cloudconnect.get_networks" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides Cloud Connect Networks available to the user.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.59.0+</p>
<p><strong>NOTE:</strong> Only the following regions support create Cloud Connect Network. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of CCN instances IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter CCN instances by name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
