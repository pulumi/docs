---
title: Module oos
title_tag: Module oos | Package pulumi_alicloud | Python SDK
linktitle: oos
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="oos">
<h1>oos<a class="headerlink" href="#oos" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.oos"></span><dl class="py class">
<dt id="pulumi_alicloud.oos.AwaitableGetTemplatesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oos.</code><code class="sig-name descname">AwaitableGetTemplatesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date_after</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_order</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">templates</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oos.AwaitableGetTemplatesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.oos.GetTemplatesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oos.</code><code class="sig-name descname">GetTemplatesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date_after</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_order</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">templates</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oos.GetTemplatesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTemplates.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.oos.GetTemplatesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.GetTemplatesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.GetTemplatesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.GetTemplatesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of OOS Template ids. Each element in the list is same as template_name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.GetTemplatesResult.templates">
<code class="sig-name descname">templates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.GetTemplatesResult.templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of OOS Templates. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.oos.Template">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.oos.</code><code class="sig-name descname">Template</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_delete_executions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oos.Template" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a OOS Template resource. For information about Alicloud OOS Template and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/120761.htm">What is Resource Alicloud OOS Template</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.92.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_executions</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When deleting a template, whether to delete its related executions. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content of the template. The template must be in the JSON or YAML format. Maximum size: 64 KB.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>template*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the template. The template name can be up to 200 characters in length. The name can contain letters, digits, hyphens (-), and underscores (<a href="#id3"><span class="problematic" id="id4">*</span></a>). It cannot start with <code class="docutils literal notranslate"><span class="pre">ALIYUN</span></code>, <code class="docutils literal notranslate"><span class="pre">ACS</span></code>, <code class="docutils literal notranslate"><span class="pre">ALIBABA</span></code>, or <code class="docutils literal notranslate"><span class="pre">ALICLOUD</span></code>.</p>
</p></li>
<li><p><strong>version_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of template version.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.auto_delete_executions">
<code class="sig-name descname">auto_delete_executions</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.auto_delete_executions" title="Permalink to this definition">¶</a></dt>
<dd><p>When deleting a template, whether to delete its related executions. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.content">
<code class="sig-name descname">content</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The content of the template. The template must be in the JSON or YAML format. Maximum size: 64 KB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.created_by">
<code class="sig-name descname">created_by</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.created_by" title="Permalink to this definition">¶</a></dt>
<dd><p>The creator of the template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.created_date">
<code class="sig-name descname">created_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the template is created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.has_trigger">
<code class="sig-name descname">has_trigger</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.has_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Is it triggered successfully.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.share_type">
<code class="sig-name descname">share_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.share_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The sharing type of the template. The sharing type of templates created by users are set to Private. The sharing type of common templates provided by OOS are set to Public.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.template_format">
<code class="sig-name descname">template_format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.template_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the template. The format can be JSON or YAML. The system automatically identifies the format.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.template_id">
<code class="sig-name descname">template_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.template_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of OOS Template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.template_name">
<code class="sig-name descname">template_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.template_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the template. The template name can be up to 200 characters in length. The name can contain letters, digits, hyphens (-), and underscores (_). It cannot start with <code class="docutils literal notranslate"><span class="pre">ALIYUN</span></code>, <code class="docutils literal notranslate"><span class="pre">ACS</span></code>, <code class="docutils literal notranslate"><span class="pre">ALIBABA</span></code>, or <code class="docutils literal notranslate"><span class="pre">ALICLOUD</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.template_type">
<code class="sig-name descname">template_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.template_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of OOS Template. <code class="docutils literal notranslate"><span class="pre">Automation</span></code> means the implementation of Alibaba Cloud API template, <code class="docutils literal notranslate"><span class="pre">Package</span></code> means represents a template for installing software.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.template_version">
<code class="sig-name descname">template_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.template_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of OOS Template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.updated_by">
<code class="sig-name descname">updated_by</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.updated_by" title="Permalink to this definition">¶</a></dt>
<dd><p>The user who updated the template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.updated_date">
<code class="sig-name descname">updated_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the template was updated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.oos.Template.version_name">
<code class="sig-name descname">version_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.oos.Template.version_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of template version.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.oos.Template.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_delete_executions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oos.Template.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Template resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_delete_executions</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When deleting a template, whether to delete its related executions. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content of the template. The template must be in the JSON or YAML format. Maximum size: 64 KB.</p></li>
<li><p><strong>created_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creator of the template.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the template is created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the template.</p></li>
<li><p><strong>has_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is it triggered successfully.</p></li>
<li><p><strong>share_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sharing type of the template. The sharing type of templates created by users are set to Private. The sharing type of common templates provided by OOS are set to Public.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>template_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the template. The format can be JSON or YAML. The system automatically identifies the format.</p></li>
<li><p><strong>template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of OOS Template.</p></li>
<li><p><strong>template*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the template. The template name can be up to 200 characters in length. The name can contain letters, digits, hyphens (-), and underscores (<a href="#id7"><span class="problematic" id="id8">*</span></a>). It cannot start with <code class="docutils literal notranslate"><span class="pre">ALIYUN</span></code>, <code class="docutils literal notranslate"><span class="pre">ACS</span></code>, <code class="docutils literal notranslate"><span class="pre">ALIBABA</span></code>, or <code class="docutils literal notranslate"><span class="pre">ALICLOUD</span></code>.</p>
</p></li>
<li><p><strong>template_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of OOS Template. <code class="docutils literal notranslate"><span class="pre">Automation</span></code> means the implementation of Alibaba Cloud API template, <code class="docutils literal notranslate"><span class="pre">Package</span></code> means represents a template for installing software.</p></li>
<li><p><strong>template_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of OOS Template.</p></li>
<li><p><strong>updated_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user who updated the template.</p></li>
<li><p><strong>updated_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the template was updated.</p></li>
<li><p><strong>version_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of template version.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.oos.Template.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oos.Template.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.oos.Template.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oos.Template.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.oos.get_templates">
<code class="sig-prename descclassname">pulumi_alicloud.oos.</code><code class="sig-name descname">get_templates</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date_after</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_field</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_order</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.oos.get_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of OOS Templates in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.92.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>category</strong> (<em>str</em>) – The category of template.</p></li>
<li><p><strong>created_by</strong> (<em>str</em>) – The creator of the template.</p></li>
<li><p><strong>created_date</strong> (<em>str</em>) – The template whose creation time is less than or equal to the specified time. The format is: YYYY-MM-DDThh:mm::ssZ.</p></li>
<li><p><strong>created_date_after</strong> (<em>str</em>) – Create a template whose time is greater than or equal to the specified time. The format is: YYYY-MM-DDThh:mm:ssZ.</p></li>
<li><p><strong>has_trigger</strong> (<em>bool</em>) – Is it triggered successfully.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of OOS Template ids. Each element in the list is same as template_name.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter the results by the template_name.</p></li>
<li><p><strong>share_type</strong> (<em>str</em>) – The sharing type of the template. Valid values: <code class="docutils literal notranslate"><span class="pre">Private</span></code>, <code class="docutils literal notranslate"><span class="pre">Public</span></code>.</p></li>
<li><p><strong>sort_field</strong> (<em>str</em>) – Sort field. Valid values: <code class="docutils literal notranslate"><span class="pre">TotalExecutionCount</span></code>, <code class="docutils literal notranslate"><span class="pre">Popularity</span></code>, <code class="docutils literal notranslate"><span class="pre">TemplateName</span></code> and <code class="docutils literal notranslate"><span class="pre">CreatedDate</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">TotalExecutionCount</span></code>.</p></li>
<li><p><strong>sort_order</strong> (<em>str</em>) – Sort order. Valid values: <code class="docutils literal notranslate"><span class="pre">Ascending</span></code>, <code class="docutils literal notranslate"><span class="pre">Descending</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">Descending</span></code></p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>template_format</strong> (<em>str</em>) – The format of the template. Valid values: <code class="docutils literal notranslate"><span class="pre">JSON</span></code>, <code class="docutils literal notranslate"><span class="pre">YAML</span></code>.</p></li>
<li><p><strong>template_type</strong> (<em>str</em>) – The type of OOS Template.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
