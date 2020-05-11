---
title: Module licensemanager
title_tag: Module licensemanager | Package pulumi_aws | Python SDK
linktitle: licensemanager
notitle: true
---

<div class="section" id="licensemanager">
<h1>licensemanager<a class="headerlink" href="#licensemanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.licensemanager"></span><dl class="py class">
<dt id="pulumi_aws.licensemanager.Association">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.licensemanager.</code><code class="sig-name descname">Association</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_configuration_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.Association" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a License Manager association.</p>
<blockquote>
<div><p><strong>Note:</strong> License configurations can also be associated with launch templates by specifying the <code class="docutils literal notranslate"><span class="pre">license_specifications</span></code> block for an <code class="docutils literal notranslate"><span class="pre">ec2.LaunchTemplate</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>license_configuration_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the license configuration.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the resource associated with the license configuration.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.Association.license_configuration_arn">
<code class="sig-name descname">license_configuration_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.Association.license_configuration_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the license configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.Association.resource_arn">
<code class="sig-name descname">resource_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.Association.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the resource associated with the license configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.licensemanager.Association.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_configuration_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.Association.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Association resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>license_configuration_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the license configuration.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the resource associated with the license configuration.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.licensemanager.Association.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.Association.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.licensemanager.Association.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.Association.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.licensemanager.LicenseConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.licensemanager.</code><code class="sig-name descname">LicenseConfiguration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_count_hard_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_counting_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a License Manager license configuration resource.</p>
<blockquote>
<div><p><strong>Note:</strong> Removing the <code class="docutils literal notranslate"><span class="pre">license_count</span></code> attribute is not supported by the License Manager API - recreate the resource instead.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">licensemanager</span><span class="o">.</span><span class="n">LicenseConfiguration</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Example&quot;</span><span class="p">,</span>
    <span class="n">license_count</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="n">license_count_hard_limit</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">license_counting_type</span><span class="o">=</span><span class="s2">&quot;Socket&quot;</span><span class="p">,</span>
    <span class="n">license_rules</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;#minimumSockets=2&quot;</span><span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;barr&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>License rules should be in the format of <code class="docutils literal notranslate"><span class="pre">#RuleType=RuleValue</span></code>. Supported rule types:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">minimumVcpus</span></code> - Resource must have minimum vCPU count in order to use the license. Default: 1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumVcpus</span></code> - Resource must have maximum vCPU count in order to use the license. Default: unbounded, limit: 10000</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumCores</span></code> - Resource must have minimum core count in order to use the license. Default: 1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumCores</span></code> - Resource must have maximum core count in order to use the license. Default: unbounded, limit: 10000</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumSockets</span></code> - Resource must have minimum socket count in order to use the license. Default: 1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumSockets</span></code> - Resource must have maximum socket count in order to use the license. Default: unbounded, limit: 10000</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedTenancy</span></code> - Defines where the license can be used. If set, restricts license usage to selected tenancies. Specify a comma delimited list of <code class="docutils literal notranslate"><span class="pre">EC2-Default</span></code>, <code class="docutils literal notranslate"><span class="pre">EC2-DedicatedHost</span></code>, <code class="docutils literal notranslate"><span class="pre">EC2-DedicatedInstance</span></code></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the license configuration.</p></li>
<li><p><strong>license_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of licenses managed by the license configuration.</p></li>
<li><p><strong>license_count_hard_limit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets the number of available licenses as a hard limit.</p></li>
<li><p><strong>license_counting_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dimension to use to track license inventory. Specify either <code class="docutils literal notranslate"><span class="pre">vCPU</span></code>, <code class="docutils literal notranslate"><span class="pre">Instance</span></code>, <code class="docutils literal notranslate"><span class="pre">Core</span></code> or <code class="docutils literal notranslate"><span class="pre">Socket</span></code>.</p></li>
<li><p><strong>license_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of configured License Manager rules.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the license configuration.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the license configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.license_count">
<code class="sig-name descname">license_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.license_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of licenses managed by the license configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.license_count_hard_limit">
<code class="sig-name descname">license_count_hard_limit</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.license_count_hard_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the number of available licenses as a hard limit.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.license_counting_type">
<code class="sig-name descname">license_counting_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.license_counting_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Dimension to use to track license inventory. Specify either <code class="docutils literal notranslate"><span class="pre">vCPU</span></code>, <code class="docutils literal notranslate"><span class="pre">Instance</span></code>, <code class="docutils literal notranslate"><span class="pre">Core</span></code> or <code class="docutils literal notranslate"><span class="pre">Socket</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.license_rules">
<code class="sig-name descname">license_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.license_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of configured License Manager rules.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the license configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_count_hard_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_counting_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LicenseConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the license configuration.</p></li>
<li><p><strong>license_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of licenses managed by the license configuration.</p></li>
<li><p><strong>license_count_hard_limit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets the number of available licenses as a hard limit.</p></li>
<li><p><strong>license_counting_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dimension to use to track license inventory. Specify either <code class="docutils literal notranslate"><span class="pre">vCPU</span></code>, <code class="docutils literal notranslate"><span class="pre">Instance</span></code>, <code class="docutils literal notranslate"><span class="pre">Core</span></code> or <code class="docutils literal notranslate"><span class="pre">Socket</span></code>.</p></li>
<li><p><strong>license_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of configured License Manager rules.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the license configuration.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.licensemanager.LicenseConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.licensemanager.LicenseConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
