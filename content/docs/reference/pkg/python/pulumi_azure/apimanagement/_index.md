---
---

<div class="section" id="module-pulumi_azure.apimanagement">
<span id="apimanagement"></span><h1>apimanagement<a class="headerlink" href="#module-pulumi_azure.apimanagement" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.apimanagement.Api">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Api</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>import_=None</em>, <em>name=None</em>, <em>path=None</em>, <em>protocols=None</em>, <em>resource_group_name=None</em>, <em>revision=None</em>, <em>service_url=None</em>, <em>soap_pass_through=None</em>, <em>subscription_key_parameter_names=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Api" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API within an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the API Management API, which may include HTML formatting tags.</li>
<li><strong>display*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The display name of the API.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] import*: A <code class="docutils literal notranslate"><span class="pre">import</span></code> block as documented below.
:param pulumi.Input[str] name: The name of the API Management API. Changing this forces a new resource to be created.
:param pulumi.Input[str] path: The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of it’s resource paths within the API Management Service.
:param pulumi.Input[list] protocols: A list of protocols the operations in this API can be invoked. Possible values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">https</span></code>.
:param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] revision: The Revision which used for this API.
:param pulumi.Input[str] service_url: Absolute URL of the backend service implementing this API.
:param pulumi.Input[bool] soap_pass_through: Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[dict] subscription_key_parameter_names: A <code class="docutils literal notranslate"><span class="pre">subscription_key_parameter_names</span></code> block as documented below.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the API Management API, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.import_">
<code class="descname">import_</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.import_" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">import</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.is_current">
<code class="descname">is_current</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.is_current" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this the current API Revision?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.is_online">
<code class="descname">is_online</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.is_online" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this API Revision online/accessible via the Gateway?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management API. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of it’s resource paths within the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.protocols">
<code class="descname">protocols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of protocols the operations in this API can be invoked. Possible values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.revision">
<code class="descname">revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The Revision which used for this API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.service_url">
<code class="descname">service_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.service_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Absolute URL of the backend service implementing this API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.soap_pass_through">
<code class="descname">soap_pass_through</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.soap_pass_through" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.subscription_key_parameter_names">
<code class="descname">subscription_key_parameter_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.subscription_key_parameter_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">subscription_key_parameter_names</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Version number of this API, if this API is versioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.version_set_id">
<code class="descname">version_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.version_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Version Set which this API is associated with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Api.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Api.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Api.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Api.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiOperation">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ApiOperation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>api_name=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>method=None</em>, <em>operation_id=None</em>, <em>request=None</em>, <em>resource_group_name=None</em>, <em>responses=None</em>, <em>template_parameters=None</em>, <em>url_template=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Operation within an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</li>
<li><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this API Operation, which may include HTML formatting tags.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name for this API Management Operation.</li>
<li><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method used for this API Management Operation, like <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> or <code class="docutils literal notranslate"><span class="pre">POST</span></code> - but not limited to these values.</li>
<li><strong>operation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for this API Operation. Changing this forces a new resource to be created.</li>
<li><strong>request</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">request</span></code> block as defined below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>responses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">response</span></code> blocks as defined below.</li>
<li><strong>template_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">template_parameter</span></code> blocks as defined below.</li>
<li><strong>url_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The relative URL Template identifying the target resource for this operation, which may include parameters.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_operation.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_operation.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.api_name">
<code class="descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this API Operation, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name for this API Management Operation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.method">
<code class="descname">method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP Method used for this API Management Operation, like <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> or <code class="docutils literal notranslate"><span class="pre">POST</span></code> - but not limited to these values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.operation_id">
<code class="descname">operation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.operation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for this API Operation. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.request">
<code class="descname">request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.request" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">request</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.responses">
<code class="descname">responses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.responses" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">response</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.template_parameters">
<code class="descname">template_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.template_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">template_parameter</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.url_template">
<code class="descname">url_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.url_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The relative URL Template identifying the target resource for this operation, which may include parameters.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiOperation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiOperation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ApiOperationPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>api_name=None</em>, <em>operation_id=None</em>, <em>resource_group_name=None</em>, <em>xml_content=None</em>, <em>xml_link=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management API Operation Policy</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management API Operation within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy.</li>
<li><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_operation_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_operation_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.api_name">
<code class="descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management API Operation within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.xml_content">
<code class="descname">xml_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.xml_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The XML Content for this Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.xml_link">
<code class="descname">xml_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.xml_link" title="Permalink to this definition">¶</a></dt>
<dd><p>A link to a Policy XML Document, which must be publicly available.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiPolicy">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ApiPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>api_name=None</em>, <em>resource_group_name=None</em>, <em>xml_content=None</em>, <em>xml_link=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management API Policy</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management API within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy.</li>
<li><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.api_name">
<code class="descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management API within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.xml_content">
<code class="descname">xml_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.xml_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The XML Content for this Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.xml_link">
<code class="descname">xml_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.xml_link" title="Permalink to this definition">¶</a></dt>
<dd><p>A link to a Policy XML Document, which must be publicly available.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiSchema">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ApiSchema</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>api_name=None</em>, <em>content_type=None</em>, <em>resource_group_name=None</em>, <em>schema_id=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Schema within an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</li>
<li><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API within the API Management Service where this API Schema should be created. Changing this forces a new resource to be created.</li>
<li><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the API Schema.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>schema_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for this API Schema. Changing this forces a new resource to be created.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON escaped string defining the document representing the Schema.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_schema.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_schema.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.api_name">
<code class="descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API within the API Management Service where this API Schema should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content type of the API Schema.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.schema_id">
<code class="descname">schema_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.schema_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for this API Schema. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON escaped string defining the document representing the Schema.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiSchema.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiSchema.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiVersionSet">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ApiVersionSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>version_header_name=None</em>, <em>version_query_name=None</em>, <em>versioning_scheme=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Version Set within a API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Version Set should exist. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of API Version Set.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Version Set.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Version Set. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the parent API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>version_header_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Header which should be read from Inbound Requests which defines the API Version.</li>
<li><strong>version_query_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Query String which should be read from Inbound Requests which defines the API Version.</li>
<li><strong>versioning_scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies where in an Inbound HTTP Request that the API Version should be read from. Possible values are <code class="docutils literal notranslate"><span class="pre">Header</span></code>, <code class="docutils literal notranslate"><span class="pre">Query</span></code> and <code class="docutils literal notranslate"><span class="pre">Segment</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_version_set.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_version_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the API Version Set should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of API Version Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Version Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Version Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the parent API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.version_header_name">
<code class="descname">version_header_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.version_header_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Header which should be read from Inbound Requests which defines the API Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.version_query_name">
<code class="descname">version_query_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.version_query_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Query String which should be read from Inbound Requests which defines the API Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.versioning_scheme">
<code class="descname">versioning_scheme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.versioning_scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies where in an Inbound HTTP Request that the API Version should be read from. Possible values are <code class="docutils literal notranslate"><span class="pre">Header</span></code>, <code class="docutils literal notranslate"><span class="pre">Query</span></code> and <code class="docutils literal notranslate"><span class="pre">Segment</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiVersionSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.AuthorizationServer">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">AuthorizationServer</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>authorization_endpoint=None</em>, <em>authorization_methods=None</em>, <em>bearer_token_sending_methods=None</em>, <em>client_authentication_methods=None</em>, <em>client_id=None</em>, <em>client_registration_endpoint=None</em>, <em>client_secret=None</em>, <em>default_scope=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>grant_types=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>resource_owner_password=None</em>, <em>resource_owner_username=None</em>, <em>support_state=None</em>, <em>token_body_parameters=None</em>, <em>token_endpoint=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Server within an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which this Authorization Server should be created. Changing this forces a new resource to be created.</li>
<li><strong>authorization_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAUTH Authorization Endpoint.</li>
<li><strong>authorization_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The HTTP Verbs supported by the Authorization Endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> and <code class="docutils literal notranslate"><span class="pre">TRACE</span></code>.</li>
<li><strong>bearer_token_sending_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The mechanism by which Access Tokens are passed to the API. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationHeader</span></code> and <code class="docutils literal notranslate"><span class="pre">query</span></code>.</li>
<li><strong>client_authentication_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Authentication Methods supported by the Token endpoint of this Authorization Server.. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Body</span></code>.</li>
<li><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client/App ID registered with this Authorization Server.</li>
<li><strong>client_registration_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of page where Client/App Registration is performed for this Authorization Server.</li>
<li><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client/App Secret registered with this Authorization Server.</li>
<li><strong>default_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Default Scope used when requesting an Access Token, specified as a string containing space-delimited values.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the Authorization Server, which may contain HTML formatting tags.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-friendly name of this Authorization Server.</li>
<li><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Form of Authorization Grants required when requesting an Access Token. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationCode</span></code>, <code class="docutils literal notranslate"><span class="pre">clientCredentials</span></code>, <code class="docutils literal notranslate"><span class="pre">implicit</span></code> and <code class="docutils literal notranslate"><span class="pre">resourceOwnerPassword</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Authorization Server. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>resource_owner_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the Resource Owner.</li>
<li><strong>resource_owner_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username associated with the Resource Owner.</li>
<li><strong>support_state</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Server support State? If this is set to <code class="docutils literal notranslate"><span class="pre">true</span></code> the client may use the state parameter to raise protocol security.</li>
<li><strong>token_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAUTH Token Endpoint.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_authorization_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_authorization_server.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which this Authorization Server should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.authorization_endpoint">
<code class="descname">authorization_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.authorization_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The OAUTH Authorization Endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.authorization_methods">
<code class="descname">authorization_methods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.authorization_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP Verbs supported by the Authorization Endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> and <code class="docutils literal notranslate"><span class="pre">TRACE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.bearer_token_sending_methods">
<code class="descname">bearer_token_sending_methods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.bearer_token_sending_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>The mechanism by which Access Tokens are passed to the API. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationHeader</span></code> and <code class="docutils literal notranslate"><span class="pre">query</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.client_authentication_methods">
<code class="descname">client_authentication_methods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.client_authentication_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>The Authentication Methods supported by the Token endpoint of this Authorization Server.. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Body</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.client_id">
<code class="descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client/App ID registered with this Authorization Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.client_registration_endpoint">
<code class="descname">client_registration_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.client_registration_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of page where Client/App Registration is performed for this Authorization Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.client_secret">
<code class="descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client/App Secret registered with this Authorization Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.default_scope">
<code class="descname">default_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.default_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The Default Scope used when requesting an Access Token, specified as a string containing space-delimited values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the Authorization Server, which may contain HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user-friendly name of this Authorization Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.grant_types">
<code class="descname">grant_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.grant_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Form of Authorization Grants required when requesting an Access Token. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationCode</span></code>, <code class="docutils literal notranslate"><span class="pre">clientCredentials</span></code>, <code class="docutils literal notranslate"><span class="pre">implicit</span></code> and <code class="docutils literal notranslate"><span class="pre">resourceOwnerPassword</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Authorization Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.resource_owner_password">
<code class="descname">resource_owner_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.resource_owner_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with the Resource Owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.resource_owner_username">
<code class="descname">resource_owner_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.resource_owner_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username associated with the Resource Owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.support_state">
<code class="descname">support_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.support_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Server support State? If this is set to <code class="docutils literal notranslate"><span class="pre">true</span></code> the client may use the state parameter to raise protocol security.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.token_endpoint">
<code class="descname">token_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.token_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The OAUTH Token Endpoint.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.AuthorizationServer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Certificate">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Certificate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>data=None</em>, <em>name=None</em>, <em>password=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Certificate within an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Service should be created. Changing this forces a new resource to be created.</li>
<li><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base-64 encoded certificate data, which must be a PFX file. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Certificate. Changing this forces a new resource to be created.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used for this certificate. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_certificate.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this Service should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.data">
<code class="descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.data" title="Permalink to this definition">¶</a></dt>
<dd><p>The base-64 encoded certificate data, which must be a PFX file. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.expiration">
<code class="descname">expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>The Expiration Date of this Certificate, formatted as an RFC3339 string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password used for this certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.subject">
<code class="descname">subject</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.subject" title="Permalink to this definition">¶</a></dt>
<dd><p>The Subject of this Certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.thumbprint">
<code class="descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Thumbprint of this Certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Certificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Certificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GetApiResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetApiResult</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>is_current=None</em>, <em>is_online=None</em>, <em>name=None</em>, <em>path=None</em>, <em>protocols=None</em>, <em>resource_group_name=None</em>, <em>revision=None</em>, <em>service_url=None</em>, <em>soap_pass_through=None</em>, <em>subscription_key_parameter_names=None</em>, <em>version=None</em>, <em>version_set_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApi.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the API Management API, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.is_current">
<code class="descname">is_current</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.is_current" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this the current API Revision?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.is_online">
<code class="descname">is_online</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.is_online" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this API Revision online/accessible via the Gateway?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The Path for this API Management API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.protocols">
<code class="descname">protocols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of protocols the operations in this API can be invoked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.service_url">
<code class="descname">service_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.service_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Absolute URL of the backend service implementing this API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.soap_pass_through">
<code class="descname">soap_pass_through</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.soap_pass_through" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this API expose a SOAP frontend, rather than a HTTP frontend?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.subscription_key_parameter_names">
<code class="descname">subscription_key_parameter_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.subscription_key_parameter_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">subscription_key_parameter_names</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Version number of this API, if this API is versioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.version_set_id">
<code class="descname">version_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.version_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Version Set which this API is associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetGroupResult</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>external_id=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.external_id">
<code class="descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the external Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this API Management Group, such as <code class="docutils literal notranslate"><span class="pre">custom</span></code> or <code class="docutils literal notranslate"><span class="pre">external</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetProductResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetProductResult</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>approval_required=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>product_id=None</em>, <em>published=None</em>, <em>resource_group_name=None</em>, <em>subscription_required=None</em>, <em>subscriptions_limit=None</em>, <em>terms=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProduct.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.approval_required">
<code class="descname">approval_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.approval_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Do subscribers need to be approved prior to being able to use the Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Product, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name for this API Management Product.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.published">
<code class="descname">published</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.published" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Product Published?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.subscription_required">
<code class="descname">subscription_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.subscription_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Is a Subscription required to access API’s included in this Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.subscriptions_limit">
<code class="descname">subscriptions_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.subscriptions_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of subscriptions a user can have to this Product at the same time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.terms">
<code class="descname">terms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>Any Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetServiceResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetServiceResult</code><span class="sig-paren">(</span><em>additional_locations=None</em>, <em>gateway_regional_url=None</em>, <em>gateway_url=None</em>, <em>hostname_configurations=None</em>, <em>location=None</em>, <em>management_api_url=None</em>, <em>name=None</em>, <em>notification_sender_email=None</em>, <em>portal_url=None</em>, <em>public_ip_addresses=None</em>, <em>publisher_email=None</em>, <em>publisher_name=None</em>, <em>resource_group_name=None</em>, <em>scm_url=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.additional_locations">
<code class="descname">additional_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.additional_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.gateway_regional_url">
<code class="descname">gateway_regional_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.gateway_regional_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Gateway URL of the API Management service in the Region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.gateway_url">
<code class="descname">gateway_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.gateway_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the API Management Service’s Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.hostname_configurations">
<code class="descname">hostname_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.hostname_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location name of the additional region among Azure Data center regions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.management_api_url">
<code class="descname">management_api_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.management_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Management API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the plan’s pricing tier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.notification_sender_email">
<code class="descname">notification_sender_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.notification_sender_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address from which the notification will be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.portal_url">
<code class="descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Publisher Portal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.public_ip_addresses">
<code class="descname">public_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.public_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.publisher_email">
<code class="descname">publisher_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.publisher_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of Publisher/Company of the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.publisher_name">
<code class="descname">publisher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.publisher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Publisher/Company of the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.scm_url">
<code class="descname">scm_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.scm_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The SCM (Source Code Management) endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetUserResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetUserResult</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>email=None</em>, <em>first_name=None</em>, <em>last_name=None</em>, <em>note=None</em>, <em>resource_group_name=None</em>, <em>state=None</em>, <em>user_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The Email Address used for this User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.first_name">
<code class="descname">first_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The First Name for the User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.last_name">
<code class="descname">last_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Last Name for the User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.note">
<code class="descname">note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.note" title="Permalink to this definition">¶</a></dt>
<dd><p>Any notes about this User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of this User, for example <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> or <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.Group">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>external_id=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Management Group should exist. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this API Management Group.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Management Group.</li>
<li><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the external Group. For example, an Azure Active Directory group <code class="docutils literal notranslate"><span class="pre">aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group</span> <span class="pre">object</span> <span class="pre">id&gt;</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Group. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Group should exist. Changing this forces a new resource to be created.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this API Management Group. Possible values are <code class="docutils literal notranslate"><span class="pre">custom</span></code> and <code class="docutils literal notranslate"><span class="pre">external</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the API Management Group should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.external_id">
<code class="descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the external Group. For example, an Azure Active Directory group <code class="docutils literal notranslate"><span class="pre">aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group</span> <span class="pre">object</span> <span class="pre">id&gt;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Group should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this API Management Group. Possible values are <code class="docutils literal notranslate"><span class="pre">custom</span></code> and <code class="docutils literal notranslate"><span class="pre">external</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GroupUser">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GroupUser</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>group_name=None</em>, <em>resource_group_name=None</em>, <em>user_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management User Assignment to a Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_group_user.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_group_user.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.group_name">
<code class="descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.user_id">
<code class="descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.GroupUser.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GroupUser.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Logger">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Logger</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>application_insights=None</em>, <em>buffered=None</em>, <em>description=None</em>, <em>eventhub=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Logger" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Logger within an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>application_insights</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">application_insights</span></code> block as documented below.</li>
<li><strong>buffered</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether records should be buffered in the Logger prior to publishing. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Logger.</li>
<li><strong>eventhub</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">eventhub</span></code> block as documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Logger, which must be unique within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_logger.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_logger.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.application_insights">
<code class="descname">application_insights</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.application_insights" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">application_insights</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.buffered">
<code class="descname">buffered</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.buffered" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether records should be buffered in the Logger prior to publishing. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this Logger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.eventhub">
<code class="descname">eventhub</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.eventhub" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">eventhub</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Logger, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Logger.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Logger.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">OpenIdConnectProvider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>client_id=None</em>, <em>client_secret=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>metadata_endpoint=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an OpenID Connect Provider within a API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which this OpenID Connect Provider should be created. Changing this forces a new resource to be created.</li>
<li><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client ID used for the Client Application.</li>
<li><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client Secret used for the Client Application.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this OpenID Connect Provider.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly name for this OpenID Connect Provider.</li>
<li><strong>metadata_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the Metadata endpoint.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the Name of the OpenID Connect Provider which should be created within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_openid_connect_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_openid_connect_provider.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which this OpenID Connect Provider should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.client_id">
<code class="descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client ID used for the Client Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.client_secret">
<code class="descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client Secret used for the Client Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this OpenID Connect Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-friendly name for this OpenID Connect Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.metadata_endpoint">
<code class="descname">metadata_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.metadata_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the Metadata endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.name" title="Permalink to this definition">¶</a></dt>
<dd><p>the Name of the OpenID Connect Provider which should be created within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Product">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Product</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>approval_required=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>product_id=None</em>, <em>published=None</em>, <em>resource_group_name=None</em>, <em>subscription_required=None</em>, <em>subscriptions_limit=None</em>, <em>terms=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Product.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>approval_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do subscribers need to be approved prior to being able to use the Product?</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Product, which may include HTML formatting tags.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name for this API Management Product.</li>
<li><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for this Product, which must be unique within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>published</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Product Published?</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</li>
<li><strong>subscription_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is a Subscription required to access API’s included in this Product?</li>
<li><strong>subscriptions_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of subscriptions a user can have to this Product at the same time.</li>
<li><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_product.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_product.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.approval_required">
<code class="descname">approval_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.approval_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Do subscribers need to be approved prior to being able to use the Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this Product, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name for this API Management Product.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.product_id">
<code class="descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for this Product, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.published">
<code class="descname">published</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.published" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Product Published?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.subscription_required">
<code class="descname">subscription_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.subscription_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Is a Subscription required to access API’s included in this Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.subscriptions_limit">
<code class="descname">subscriptions_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.subscriptions_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of subscriptions a user can have to this Product at the same time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.terms">
<code class="descname">terms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>The Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Product.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Product.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductApi">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ProductApi</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>api_name=None</em>, <em>product_id=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management API Assignment to a Product.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management API within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_product_api.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_product_api.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductApi.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductApi.api_name">
<code class="descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management API within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductApi.product_id">
<code class="descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductApi.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductApi.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductApi.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ProductGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>group_name=None</em>, <em>product_id=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Product Assignment to a Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_product_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_product_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.group_name">
<code class="descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.product_id">
<code class="descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductPolicy">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ProductPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>product_id=None</em>, <em>resource_group_name=None</em>, <em>xml_content=None</em>, <em>xml_link=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Product Policy</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy.</li>
<li><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_product_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_product_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.product_id">
<code class="descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.xml_content">
<code class="descname">xml_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.xml_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The XML Content for this Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.xml_link">
<code class="descname">xml_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.xml_link" title="Permalink to this definition">¶</a></dt>
<dd><p>A link to a Policy XML Document, which must be publicly available.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Property">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Property</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>display_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>secret=None</em>, <em>tags=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Property.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Management Property should exist. Changing this forces a new resource to be created.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Management Property.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Property. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Property should exist. Changing this forces a new resource to be created.</li>
<li><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the API Management Property is secret. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to be applied to the API Management Property.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of this API Management Property.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_property.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_property.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the API Management Property should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Property. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Property should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.secret">
<code class="descname">secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the API Management Property is secret. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to be applied to the API Management Property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of this API Management Property.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Property.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Property.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Service">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Service</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>additional_location=None</em>, <em>certificates=None</em>, <em>hostname_configuration=None</em>, <em>identity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>notification_sender_email=None</em>, <em>policy=None</em>, <em>publisher_email=None</em>, <em>publisher_name=None</em>, <em>resource_group_name=None</em>, <em>security=None</em>, <em>sign_in=None</em>, <em>sign_up=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>additional_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below.</li>
<li><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</li>
<li><strong>hostname_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block is documented below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>notification_sender_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address from which the notification will be sent.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">policy</span></code> block as defined below.</li>
<li><strong>publisher_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of publisher/company.</li>
<li><strong>publisher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of publisher/company.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</li>
<li><strong>security</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">security</span></code> block as defined below.</li>
<li><strong>sign_in</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sign_in</span></code> block as defined below.</li>
<li><strong>sign_up</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sign_up</span></code> block as defined below.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags assigned to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.additional_location">
<code class="descname">additional_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.additional_location" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.certificates">
<code class="descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.gateway_regional_url">
<code class="descname">gateway_regional_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.gateway_regional_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Regional Gateway for the API Management Service in the specified region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.gateway_url">
<code class="descname">gateway_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.gateway_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Gateway for the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.hostname_configuration">
<code class="descname">hostname_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.hostname_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.management_api_url">
<code class="descname">management_api_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.management_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Management API associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.notification_sender_email">
<code class="descname">notification_sender_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.notification_sender_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address from which the notification will be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">policy</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.portal_url">
<code class="descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Publisher Portal associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.public_ip_addresses">
<code class="descname">public_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.public_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.publisher_email">
<code class="descname">publisher_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.publisher_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of publisher/company.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.publisher_name">
<code class="descname">publisher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.publisher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of publisher/company.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.scm_url">
<code class="descname">scm_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.scm_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.security">
<code class="descname">security</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.security" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">security</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.sign_in">
<code class="descname">sign_in</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.sign_in" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sign_in</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.sign_up">
<code class="descname">sign_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.sign_up" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sign_up</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Service.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Service.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Subscription">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Subscription</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>display_name=None</em>, <em>primary_key=None</em>, <em>product_id=None</em>, <em>resource_group_name=None</em>, <em>secondary_key=None</em>, <em>state=None</em>, <em>subscription_id=None</em>, <em>user_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Subscription within a API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service where this Subscription should be created. Changing this forces a new resource to be created.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this Subscription.</li>
<li><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Product which should be assigned to this Subscription. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of this Subscription. Possible values are <code class="docutils literal notranslate"><span class="pre">Active</span></code>, <code class="docutils literal notranslate"><span class="pre">Cancelled</span></code>, <code class="docutils literal notranslate"><span class="pre">Expired</span></code>, <code class="docutils literal notranslate"><span class="pre">Rejected</span></code>, <code class="docutils literal notranslate"><span class="pre">Submitted</span></code> and <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Submitted</span></code>.</li>
<li><strong>subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Identifier which should used as the ID of this Subscription. If not specified a new Subscription ID will be generated. Changing this forces a new resource to be created.</li>
<li><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the User which should be assigned to this Subscription. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_subscription.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service where this Subscription should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this Subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.product_id">
<code class="descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Product which should be assigned to this Subscription. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of this Subscription. Possible values are <code class="docutils literal notranslate"><span class="pre">Active</span></code>, <code class="docutils literal notranslate"><span class="pre">Cancelled</span></code>, <code class="docutils literal notranslate"><span class="pre">Expired</span></code>, <code class="docutils literal notranslate"><span class="pre">Rejected</span></code>, <code class="docutils literal notranslate"><span class="pre">Submitted</span></code> and <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Submitted</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.subscription_id">
<code class="descname">subscription_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An Identifier which should used as the ID of this Subscription. If not specified a new Subscription ID will be generated. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.user_id">
<code class="descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the User which should be assigned to this Subscription. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Subscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Subscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.User">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>confirmation=None</em>, <em>email=None</em>, <em>first_name=None</em>, <em>last_name=None</em>, <em>note=None</em>, <em>password=None</em>, <em>resource_group_name=None</em>, <em>state=None</em>, <em>user_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management User.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the User should be created. Changing this forces a new resource to be created.</li>
<li><strong>confirmation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of confirmation email which will be sent to this user. Possible values are <code class="docutils literal notranslate"><span class="pre">invite</span></code> and <code class="docutils literal notranslate"><span class="pre">signup</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address associated with this user.</li>
<li><strong>first_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first name for this user.</li>
<li><strong>last_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last name for this user.</li>
<li><strong>note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note about this user.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with this user.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of this user. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> and <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</li>
<li><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for this User, which must be unique within the API Management Service. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_user.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_user.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the User should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.confirmation">
<code class="descname">confirmation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.confirmation" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of confirmation email which will be sent to this user. Possible values are <code class="docutils literal notranslate"><span class="pre">invite</span></code> and <code class="docutils literal notranslate"><span class="pre">signup</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address associated with this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.first_name">
<code class="descname">first_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The first name for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.last_name">
<code class="descname">last_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The last name for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.note">
<code class="descname">note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.note" title="Permalink to this definition">¶</a></dt>
<dd><p>A note about this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of this user. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> and <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.user_id">
<code class="descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for this User, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_api">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_api</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>revision=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_api" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management API.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_api.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_api.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_group">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_group</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Group.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_group.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_product">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_product</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>product_id=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_product" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Product.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_product.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_product.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_service">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_service</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Service.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_user">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_user</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>resource_group_name=None</em>, <em>user_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management User.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_user.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_user.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
